# Compound V skills

`compound-v-plan`, `compound-v-execute`, and `compound-v-review` handle individual phases. `compound-v-pipeline` connects them when implementation is authorized. Supporting skills cover persistence, dependency analysis, testing, debugging, and verification. `herd.json` declares the dependency closure so selected workflows retain their helpers.

Native workflow entry points are manual; helpers remain callable during an authorized pipeline. No skill assumes a particular host tool name, worker count, model, or permission bypass.
