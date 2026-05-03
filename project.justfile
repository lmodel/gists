## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Run comprehensive unit tests with coverage
[group('testing')]
@test-unit:
    uv run python -m pytest tests/ -v --tb=short

# Run unit tests with coverage report
[group('testing')]
@test-coverage:
    uv run python -m pytest tests/ -v --cov=src/gist --cov-report=html --cov-report=term

# Run specific test file or module
[group('testing')]
@test-file file='tests/':
    uv run python -m pytest {{file}} -v --tb=short

# Run data validation tests
[group('testing')]
@test-data:
    uv run python -m pytest tests/test_data.py -v --tb=short

# Run schema validation tests
[group('testing')]
@test-schema:
    uv run python -m pytest tests/test_schema_validation.py -v --tb=short

# Run OWL to LinkML conversion tests
[group('testing')]
@test-owl:
    uv run python -m pytest tests/test_owl_to_linkml.py -v --tb=short

# Run SHACL shapes validation tests
[group('testing')]
@test-shacl:
    uv run python -m pytest tests/test_shacl_validation.py -v --tb=short

# Run generated artifacts tests
[group('testing')]
@test-artifacts:
    uv run python -m pytest tests/test_generated_artifacts.py -v --tb=short

# Run all tests with linting
[group('testing')]
@test-all: lint test-unit
    @echo "All tests passed!"

# Run tests in watch mode (requires pytest-watch)
[group('testing')]
@test-watch:
    uv run python -m pytest_watch tests/ -v --tb=short || uv run python -m pip install pytest-watch && uv run python -m pytest_watch tests/ -v --tb=short

