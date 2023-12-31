import unittest
import flask_testing
import json
import sys
from datetime import datetime, date
sys.path.append('../../backend')
from app import app
from database import db
from models.access_rights import AccessRights
from models.category import Category
from models.job_application import JobApplication
from models.login_details import LoginDetails
from models.role_listing import RoleListing
from models.role_skill import RoleSkill
from models.role import Role
from models.skills import Skill
from models.staff import Staff
from models.staff_skill import StaffSkill

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://" # In-memory database
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {} 
    app.config['TESTING'] = True # Disable error catching during request handling

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()
        self.maxDiff = None

        staff = Staff(staff_id = 1, staff_fname = "john", staff_lname = "tan", dept = "IT", country="singapore", email="johntan@email.com", role=1) 
        staff1 = Staff(staff_id = 2, staff_fname = "olivia", staff_lname = "lim", dept = "Sales", country="singapore", email="olivialim@email.com", role=1) 


        category = Category(category = "IT",category_desc ="information systems")
        category1 = Category(category = "Finance",category_desc ="financial systems")


        role = Role(role_name = "Software Engineer", role_desc = "Develops software")
        role1 = Role(role_name = "Support Engineer", role_desc = "Supports software")

        role_listing = RoleListing(listing_id = 1, role_name = "Software Engineer", category = "IT", department="IT", deadline = date(2024, 5, 17))
        role_listing2 = RoleListing(listing_id = 2, role_name = "Support Engineer", category = "IT", department="IT", deadline = date(2024, 5, 17))

        
        role_skill1 = RoleSkill(role_name = "Software Engineer", skill_name = "Python")
        role_skill2 = RoleSkill(role_name = "Software Engineer", skill_name = "database management")
        role_skill3 = RoleSkill(role_name = "Software Engineer", skill_name = "scrum methodology")
        role_skill4 = RoleSkill(role_name = "Software Engineer", skill_name = "data structures and algorithms")

        role_skill5 = RoleSkill(role_name = "Support Engineer", skill_name = "Python")
        role_skill6 = RoleSkill(role_name = "Support Engineer", skill_name = "scrum methodology")
        role_skill7 = RoleSkill(role_name = "Support Engineer", skill_name = "data structures and algorithms")


        jobapplication1 = JobApplication(application_id = 1, staff_id = 1, listing_id = 1, application_date = date(2023, 5, 17))

        db.session.add(staff)
        db.session.add(staff1)
        db.session.add(role)
        db.session.add(role1)
        db.session.add(role_listing)
        db.session.add(role_listing2)
        db.session.add(category)
        db.session.add(category1)
        db.session.add(role_skill1)
        db.session.add(role_skill2)
        db.session.add(role_skill3)
        db.session.add(role_skill4)
        db.session.add(role_skill5)
        db.session.add(role_skill6)
        db.session.add(role_skill7)
        db.session.add(jobapplication1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestRoleListing(TestApp):
    def test_get_all_role_listings(self):
        response = self.client.get('/hr/role_listings')
        data = json.loads(response.data)
        
        # Assert the status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the response data matches what is expected
        expected_data = {
            "code": 200,
            "data": {
                "role_listing": [
                    {
                        "listing_id": 1,
                        "role_name": "Software Engineer",
                        "category": "IT",
                        "department": "IT",
                        "deadline": "2024-05-17",
                        "skills_required": ["Python", "database management", "scrum methodology", "data structures and algorithms"],
                        "role_desc": ["Develops software"]
                    },
                    {
                        "listing_id": 2,
                        "role_name": "Support Engineer",
                        "category": "IT",
                        "department": "IT",
                        "deadline": "2024-05-17",
                        "skills_required": ["Python", "scrum methodology", "data structures and algorithms"],
                        "role_desc": ["Supports software"]
                    }
                ]
            }
        }

        self.assertListEqual(sorted(data['data']['role_listing'][0]['skills_required']), sorted(expected_data['data']['role_listing'][0]['skills_required']))
        self.assertListEqual(sorted(data['data']['role_listing'][1]['skills_required']), sorted(expected_data['data']['role_listing'][1]['skills_required']))


    def test_get_one_role_listings_valid_id(self):
        response = self.client.get('/hr/role_listings/1')
        data = json.loads(response.data)

        # Assert the status code is 200
        self.assertEqual(response.status_code, 200)

        # Assert that the response data matches what is expected
        expected_data = {
            "code": 200,
            "data": {
                "role_listing": {
                    "listing_id": 1,
                    "role_name": "Software Engineer",
                    "category": "IT",
                    "department": "IT",
                    "deadline": "2024-05-17",
                    "skills_required": ["Python", "database management", "scrum methodology", "data structures and algorithms"],
                    "role_desc": ["Develops software"]
                }
            }
        }

        self.assertListEqual(sorted(data['data']['role_listing']['skills_required']), sorted(expected_data['data']['role_listing']['skills_required']))

    def test_get_one_role_listings_invalid_id(self):
        response = self.client.get('/hr/role_listings/99') # Assume 99 is an invalid ID
        data = json.loads(response.data)

        # Assert the status code is 404
        self.assertEqual(response.status_code, 404)

        # Assert that the response data matches what is expected for an invalid ID
        expected_data = {
            "code": 404,
            "message": "There is no such role listing"
        }

        self.assertDictEqual(data, expected_data)

    def test_get_role_listings_not_applied(self):
        response = self.client.get('/staff/role_listings/1')
        data = json.loads(response.data)

        # Assert that the status code is 200 (i.e., the API endpoint returns some listings)
        self.assertEqual(response.status_code, 200)

        # Assert the structure of the returned data matches expectations
        role_listings_with_skill_match = data.get("data", {}).get("role_listings_with_skill_match", [])

        for listing in role_listings_with_skill_match:
            self.assertIn("role_listing", listing)
            self.assertIn("role_skill_match", listing)
            self.assertIn("have", listing["role_skill_match"])
            self.assertIn("dont", listing["role_skill_match"])
            self.assertIn("match_percentage", listing["role_skill_match"])

    def test_browse_listing_valid_search(self):
        response = self.client.get('/staff/browse_role_listings/2/software')
        data = json.loads(response.data)

        # Assert that the status code is 200 (i.e., the API endpoint returns some listings)
        self.assertEqual(response.status_code, 200)

        # Assert the structure of the returned data matches expectations
        role_listings_with_skill_match = data.get("data", {}).get("role_listings_with_skill_match", [])

        for listing in role_listings_with_skill_match:
            self.assertIn("role_listing", listing)
            self.assertIn("role_skill_match", listing)
            self.assertIn("have", listing["role_skill_match"])
            self.assertIn("dont", listing["role_skill_match"])
            self.assertIn("match_percentage", listing["role_skill_match"])

    def test_browse_listing_invalid_search(self):
        # Test with an invalid search input containing numbers, e.g., "dev123"
        response = self.client.get('/staff/browse_role_listings/1/dev123')
        data = json.loads(response.data)

        # Assert that the status code is 400 (i.e., invalid search input)
        self.assertEqual(response.status_code, 400)

        # Assert that the message indicates the search input was invalid
        self.assertEqual(data.get("message"), "Search input contains invalid characters or numbers.")

    def test_browse_listing_no_match(self):
        response = self.client.get('/staff/browse_role_listings/1/zombie')
        data = json.loads(response.data)

        # Assert that the status code is 404 (i.e., no listings found)
        self.assertEqual(response.status_code, 404)

        # Assert that the message indicates no role listings were found for the search input
        self.assertEqual(data.get("message"), "There are no role listings matching your query.")

    def test_update_valid_role_listing(self):
        # Test updating a valid role listing's name
        response = self.client.put('/hr/update_role_listing/1', json={
            'role_name': 'Senior Software Engineer'
        })

        data = json.loads(response.data)

        # Assert that the status code is 200 (i.e., the update was successful)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data.get("code"), 200)
        self.assertEqual(data.get("message"), "Successfully updated role listing!")
        self.assertEqual(data["data"]["role_name"], "Senior Software Engineer")

    def test_update_to_duplicate_role_listing(self):
        # Test updating to a duplicate role listing (same as role_listing2)
        response = self.client.put('/hr/update_role_listing/1', json={
            'role_name': 'Support Engineer',
            'category': 'IT',
            'department': 'IT'
        })

        data = json.loads(response.data)

        # Assert that the status code is 400 (i.e., the update would create a duplicate)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Duplicate role listing after update")

    def test_update_with_invalid_deadline(self):
        # Test updating with a past deadline
        response = self.client.put('/hr/update_role_listing/1', json={
            'deadline': '2022-01-01'
        })

        data = json.loads(response.data)

        # Assert that the status code is 400 (i.e., the deadline is in the past)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data.get("error"), "Deadline must be in the future")

    def test_update_nonexistent_role_listing(self):
        # Test updating a role listing that doesn't exist
        response = self.client.put('/hr/update_role_listing/100', json={
            'role_name': 'Senior Software Engineer'
        })

        data = json.loads(response.data)

        # Assert that the status code is 404 (i.e., the role listing was not found)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data.get("error"), "Role listing not found")
        
if __name__ == '__main__':
    unittest.main()