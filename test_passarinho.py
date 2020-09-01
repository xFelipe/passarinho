# import tempfile
# import os
#
# import pytest
# from passarinho import app as main
#
#
# @pytest.fixture
# def client():
#     db_fd, main.app.config['DATABASE'] = tempfile.mkstemp()
#     main.app.config['TESTING'] = True
#
#     with main.app.test_client() as client:
#         with main.app.app_context():
#             main.init_db()
#         yield client
#
#     os.close(db_fd)
#     os.unlink(main.app.config['DATABASE'])
