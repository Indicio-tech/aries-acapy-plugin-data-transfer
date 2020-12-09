ACA-Py Plugin - Data Transfer
=============================

More details to come.

### `provide-data`

Example:
```json
{
  "@type": "https://didcomm.org/data-transfer/0.1/provide-data",
  "@id": "c783e26d-68e3-412f-b120-aa955f00b23b",
  "goal_code": "test_goal",
  "data~attach": [
    {
	  "description": "test data attachment",
	  "data": {
	    "json": {"test": "data"}
	  }
	}
  ]
}
```
