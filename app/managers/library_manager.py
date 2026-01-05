class LibraryManager:

    @staticmethod
    async def get_all_libraries():
        return {
            "success": True,
            "data": [
                {
                    "id" : 1,
                    "name": "Learn Well Library",
                    "location": "Sector 66, Badshahpur",
                    "manager": "Prem Singh"
                },
                {
                    "id" : 2,
                    "name": "Achievers Library",
                    "location": "MG Road, Gurugram",
                    "manager": "Ram Shankar"
                }
            ]
        }
    
    @staticmethod
    async def get_all_books_from_library(library_id: int):
        return {
            "success": True,
            "data": [
                {
                    "id": "1",
                    "name": "The Theory of Everything",
                    "author": "Stephan J Hawkings",
                    "rating": "10",
                },
                {
                    "id": "2",
                    "name": "The Wings of Fire",
                    "author": "Dr. APJ Abdul Kalam",
                    "rating": "10",
                }
            ]
        }
