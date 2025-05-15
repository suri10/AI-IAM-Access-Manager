
#!/bin/bash
mkdir -p docs
curl http://127.0.0.1:8000/openapi.json -o docs/openapi.json
echo "Docs exported to docs/openapi.json"
