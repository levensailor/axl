"""
Unified Communications server will be required for these tests
Tests are performed against UCM 10.5.2
"""
import unittest

from axl.foley import AXL


wsdl = 'file:///Users/brad/Documents/code/python/axl/axlsqltoolkit/schema/10.5/AXLAPI.wsdl'
ucm = AXL('admin', 'asdfpoiu', wsdl, '192.168.200.10')


class TestAXL(unittest.TestCase):

    # Location
    def test_add_location_and_delete_location_is_successful(self):
        add_loc = ucm.add_location('test_location')
        del_loc = ucm.delete_location('test_location')
        self.assertEqual(add_loc['success'], True) and self.assertEqual(del_loc['success'], True)

    def test_add_duplicate_location_fails(self):
            location = 'test_dup_location'
            ucm.add_location(location)
            duplicate = ucm.add_location(location)

            # clean up
            ucm.delete_location(location)

            self.assertEqual(duplicate['success'], False) and self.assertIn(duplicate['msg'], 'already exists')

    def test_delete_non_existing_location_fails(self):
        location = 'location_dont_exist'
        result = ucm.delete_location(location)
        self.assertEqual(result['success'], False) and self.assertIn(result['msg'], 'not found')

    # Region
    def test_add_region_and_delete_region_is_successful(self):
        add_reg = ucm.add_region('test_region')
        del_reg = ucm.delete_region('test_region')
        self.assertEqual(add_reg['success'], True) and self.assertEqual(del_reg['success'], True)

    def test_add_duplicate_region_fails(self):
            region = 'test_dup_region'
            ucm.add_region(region)
            duplicate = ucm.add_region(region)

            # clean up
            ucm.delete_region(region)

            self.assertEqual(duplicate['success'], False) and self.assertIn(duplicate['msg'], 'already exists')

    def test_delete_non_existing_region_fails(self):
        region = 'region_dont_exist'
        result = ucm.delete_region(region)
        self.assertEqual(result['success'], False) and self.assertIn(result['msg'], 'not found')

    # SRST
    def test_add_srst_and_delete_srst_is_successful(self):
        add_srst = ucm.add_srst('test_srst', '192.168.100.100')
        del_srst = ucm.delete_srst('test_srst')
        self.assertEqual(add_srst['success'], True) and self.assertEqual(del_srst['success'], True)

    def test_add_duplicate_srst_fails(self):
            srst = 'test_dup_srst'
            ucm.add_srst(srst, '192.168.100.100')
            duplicate = ucm.add_srst(srst, '192.168.100.100')

            # clean up
            ucm.delete_srst(srst)

            self.assertEqual(duplicate['success'], False) and self.assertIn(duplicate['msg'], 'already exists')

    def test_delete_non_existing_srst_fails(self):
        srst = 'srst_dont_exist'
        result = ucm.delete_srst(srst)
        self.assertEqual(result['success'], False) and self.assertIn(result['msg'], 'not found')

    # Device Pool
    def test_add_device_pool_and_delete_device_pool_is_successful(self):
        device_pool = 'test_device_pool'
        add_device_pool = ucm.add_device_pool(device_pool)
        del_device_pool = ucm.delete_device_pool(device_pool)

        self.assertEqual(add_device_pool['success'], True) and self.assertEqual(del_device_pool['success'], True)

    def test_add_duplicate_device_pool_fails(self):
            device_pool = 'test_dup_device_pool'
            ucm.add_device_pool(device_pool)
            duplicate = ucm.add_device_pool(device_pool)

            # clean up
            ucm.delete_device_pool(device_pool)

            self.assertEqual(duplicate['success'], False) and self.assertIn(duplicate['msg'], 'already exists')

    def test_delete_non_existing_device_pool_fails(self):
        device_pool = 'dp_dont_exist'
        result = ucm.delete_device_pool(device_pool)
        self.assertEqual(result['success'], False) and self.assertIn(result['msg'], 'not found')