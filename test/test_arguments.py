import os
import sys
sys.path.append(os.environ["INTENTPRED_PATH"])

import unittest

from utils import argument_utils, defaults

class TestArguments(unittest.TestCase):
    def test_defaults(self):
        args = argument_utils.parse_args(parse_args=False)
        self.assertEqual(args.mode, defaults.MODE)
        self.assertEqual(args.filename, defaults.FILENAME)
        self.assertEqual(args.featurize_type, defaults.FEATURIZE_TYPE)
        self.assertEqual(args.test_nums, defaults.TEST_NUMS)
        self.assertEqual(args.test_intersections, defaults.TEST_INTERSECTIONS)

    def test_non_defaults(self):
        mode = "evaluate"
        filename = "testfile"
        featurize = "n"
        testnums = "000,001,111"
        test_intersections = "1,2,3,4"

        nondefault_arglist = [
            mode,
            "--filename", filename,
            "--featurize", featurize,
            "--test_nums", testnums,
            "--test_intersections", test_intersections
        ]

        args = argument_utils.parse_args(parse_args=False, arglist=nondefault_arglist)
        self.assertEqual(args.mode, mode)
        self.assertEqual(args.filename, filename)
        self.assertEqual(args.featurize_type, featurize)
        self.assertEqual(args.test_nums, testnums)
        self.assertEqual(args.test_intersections, test_intersections)

    def test_flags(self):
        flag_shorthand_arglist = ["evaluate", "-d", "-s", "-q", "-l", "-x"]
        args = argument_utils.parse_args(parse_args=False, arglist=flag_shorthand_arglist)
        self.assertTrue(args.make_distance_histograms)
        self.assertTrue(args.save_scores)
        self.assertTrue(args.quiet_eval)
        self.assertTrue(args.load_scores)
        self.assertTrue(args.excel)

        flag_longhand_arglist = [
            "evaluate", 
            "--make_distance_histograms", 
            "--save_scores", 
            "--quiet_eval", 
            "--load_scores", 
            "--excel"]

        args = argument_utils.parse_args(parse_args=False, arglist=flag_longhand_arglist)
        self.assertTrue(args.make_distance_histograms)
        self.assertTrue(args.save_scores)
        self.assertTrue(args.quiet_eval)
        self.assertTrue(args.load_scores)
        self.assertTrue(args.excel)
    
    #def test_invalid_options(self):

if __name__ == '__main__':
    unittest.main()