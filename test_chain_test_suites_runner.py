if __name__ == "__main__":
    import unittest
    from test_chain_test_suites import *
    suite1 = unittest.TestLoader().loadTestsFromTestCase( \
        RomanNumeralConverterTest)
    suite2 = unittest.TestLoader().loadTestsFromTestCase( \
        RomanNumeralComboTest)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)