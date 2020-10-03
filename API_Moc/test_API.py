from unittest.mock import patch, MagicMock
from API_Moc.API_moc import get_only_numbers, API

def test_api_read_only_numbers():
    test_data = ["1,2,4,5,6,ab,c21,v3234f","421,23,42"]
    expected = "1|2|4|5|6|421|23|42"

    fake_api = MagicMock()
    fake_api.get_data.return_value = test_data
    with patch('API_Moc.API_moc.API',fake_api):
        result =get_only_numbers()
        assert result == expected



