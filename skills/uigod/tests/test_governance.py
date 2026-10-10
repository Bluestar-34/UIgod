"""Check sync preservation and classification boundaries using an isolated library."""
import unittest,tempfile,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from library_data import compile_catalog,register_new,read,write,check_source_removals

class GovernanceTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        (self.root/'skills/style-manager/styles').mkdir(parents=True)
        self.collection=self.root/'collections/test';self.collection.mkdir(parents=True)
        (self.collection/'data').mkdir()
        write(self.collection/'IMPORT.json',{'upstream':'https://example.org/source','commit':'abc','record_count':1})
        self.record={'slug':'sample-123456','author':'creator','author_url':'https://example.org/creator','category':'3d','tech_tags':['threejs'],'prompt':'Exact original prompt','prompt_partial':True,'post_url':'https://example.org/post','poster_url':'https://example.org/poster'}
        write(self.collection/'data/videos.json',[self.record])
        self.id='opus-external-'+self.record['slug']
        self.manual={'added_at':'2025-01-01T00:00:00+00:00','updated_at':'2025-02-01T00:00:00+00:00','display_name':'网点空间','summary':'人工整理的中文简介','visual_tags':['黑白网点']}
        write(self.root/'editorial.json',{'entries':{self.id:self.manual}})

    def test_sync_preserves_human_edits_and_first_added_date(self):
        self.record['prompt']='Updated upstream prompt'
        write(self.collection/'data/videos.json',[self.record])
        register_new(self.root)
        self.assertEqual(read(self.root/'editorial.json')['entries'][self.id],self.manual)
        entry=compile_catalog(self.root)['entries'][0]
        self.assertEqual(entry['prompt_text'],'Updated upstream prompt')
        self.assertEqual(entry['display_name'],'网点空间')
        self.assertEqual(entry['added_at'],self.manual['added_at'])

    def test_three_dimensions_do_not_invent_content_purpose(self):
        entry=compile_catalog(self.root)['entries'][0]
        self.assertEqual(entry['content_type'],'待分类')
        self.assertEqual(entry['tech_tags'],['threejs'])
        self.assertEqual(entry['status'],'imported-unverified')

    def test_editorial_cannot_overwrite_creator_or_raw_prompt(self):
        self.manual['author']='false-credit'
        write(self.root/'editorial.json',{'entries':{self.id:self.manual}})
        with self.assertRaises(ValueError):compile_catalog(self.root)

    def test_interactive_reference_does_not_imply_game(self):
        self.record['category']='interactive'
        write(self.collection/'data/videos.json',[self.record])
        entry=compile_catalog(self.root)['entries'][0]
        self.assertIn('interactive',entry['media'])
        self.assertEqual(entry['content_type'],'待分类')

    def test_new_ids_get_dates_without_changing_old_ids(self):
        next_record=dict(self.record,slug='new-654321')
        write(self.collection/'data/videos.json',[self.record,next_record])
        register_new(self.root)
        ledger=read(self.root/'editorial.json')['entries']
        self.assertEqual(ledger[self.id],self.manual)
        self.assertIn('added_at',ledger['opus-external-new-654321'])
        self.assertEqual(len(compile_catalog(self.root)['entries']),2)

    def test_source_removal_stops_before_implicit_deletion(self):
        with self.assertRaises(ValueError):check_source_removals([self.record],[])
        check_source_removals([self.record],[self.record,dict(self.record,slug='another')])

if __name__=='__main__':unittest.main()
