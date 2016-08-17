import os

from bears.documentation.DocumentationStyleBear import DocumentationStyleBear
from tests.LocalBearTestHelper import verify_local_bear


def load_testfile(test, filename):
    filepath = os.path.join(os.path.dirname(__file__), "test_files",
                            "DocumentationStyleBear", filename)
    with open(filepath) as fl:
        return fl.read()

good_file = load_testfile("DocumentationStyleBear", "good_file.py")
bad_file = load_testfile("DocumentationStyleBear", "bad_file.py")

DocumentationStyleBear = verify_local_bear(DocumentationStyleBear,
                                           valid_files=(good_file,),
                                           invalid_files=(bad_file,),
                                           settings={'language': 'python',
                                                     'docstyle': 'default'})
