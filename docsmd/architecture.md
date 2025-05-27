# Architecture Documentation

## Overview

`mypy-boto3-builder` is a code generator that creates type annotations for AWS SDK libraries (boto3, aioboto3, aiobotocore). It introspects AWS service definitions and generates Python type stubs, enabling static type checking for AWS SDK usage.

## High-Level Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   AWS Service   │    │     Parser      │    │   Generator     │
│   Definitions   │───▶│    (Extract)    │───▶│   (Transform)   │
│   (botocore)    │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                                                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│    Generated    │    │    Templates    │    │   Structures    │
│   Type Stubs    │◀───│    (Jinja2)     │◀───│  (Data Model)   │
│   (.pyi files)  │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Core Components

### 1. Parsers (`/parsers/`)

**Purpose**: Extract and interpret AWS service definitions from botocore

**Key Classes**:
- `ShapeParser` - Converts botocore shapes to internal type representations
- `ClientParser` - Extracts client methods and their signatures
- `ResourceParser` - Handles boto3 resource definitions
- `ServicePackageParser` - Orchestrates parsing for a complete service

**Flow**:
```python
# Example parsing flow
service_model = boto3.Session().get_service_model('s3')
parser = ServicePackageParser(service_model)
service_package = parser.parse()  # Returns ServicePackage structure
```

### 2. Structures (`/structures/`)

**Purpose**: Internal data model representing AWS services and their components

**Key Classes**:
- `ServicePackage` - Complete service definition (client, resources, paginators, etc.)
- `Client` - Service client with methods and attributes
- `Method` - Individual service operation with arguments and return types
- `TypeAnnotation` - Type system for generating Python type hints

**Design Pattern**: Data Transfer Objects (DTOs) with behavior

### 3. Generators (`/generators/`)

**Purpose**: Convert internal structures to target library formats

**Key Classes**:
- `BaseGenerator` - Common generation logic and template management
- `TypesBoto3Generator` - types-boto3 packages generation
- `Boto3Generator` - obsolete boto3-stubs packages generation
- `AioBoto3Generator` - types-aioboto3 packages generation
- `AioBotocoreGenerator` - types-aioboto3 packages generation

**Strategy Pattern**: Each generator implements the same interface but produces different outputs

### 4. Templates (`/templates/`)

**Purpose**: Jinja2 templates for generating Python code

**Organization**:
```
templates/
├── common/           # Shared templates
│   ├── service/      # Individual service templates
│   └── wrapper/      # Multi-service package templates
├── boto3/           # boto3-specific templates
├── types-boto3/     # types-boto3 stub templates
└── ...
```

### 5. Type Annotations (`/type_annotations/`)

**Purpose**: Abstract type system for generating Python type hints

**Key Classes**:
- `TypeAnnotation` - Base type representation
- `TypeSubscript` - Generic types (List[str], Dict[str, Any])
- `TypeUnion` - Union types (str | int)
- `TypeTypedDict` - Structured dictionary types

## Data Flow

### 1. Service Discovery
```python
# Discover available AWS services
service_names = get_available_service_names()
# Returns: ['s3', 'ec2', 'lambda', ...]
```

### 2. Parsing Phase
```python
# For each service:
service_model = session.get_service_model(service_name)
parser = ServicePackageParser(service_model, service_name)
service_package = parser.parse()
```

### 3. Generation Phase
```python
# Transform to target format:
generator = Boto3Generator()
package = generator.generate_service_package(service_package)
```

### 4. Template Rendering
```python
# Render to Python code:
writer = PackageWriter(output_path)
writer.write_service_package(package, templates_path)
```

## Key Design Patterns

### 1. Template Method Pattern
`BaseGenerator` defines the generation algorithm, subclasses customize specific steps:

```python
class BaseGenerator:
    def generate_service_package(self, service_package):
        # Template method
        self._setup_imports()
        self._generate_client()
        self._generate_resources()
        return self._finalize_package()
    
    def _generate_client(self):
        # Abstract method - subclasses implement
        raise NotImplementedError
```

### 2. Builder Pattern
Complex objects like `ServicePackage` are built incrementally:

```python
class ServicePackageBuilder:
    def add_client(self, client): ...
    def add_resources(self, resources): ...
    def build(self) -> ServicePackage: ...
```

### 3. Strategy Pattern
Different generators for different target libraries:

```python
generators = {
    'types-boto3': TypesBoto3Generator(),
    'aioboto3': AioBoto3Generator(),
    'aiobotocore': AioBotocoreGenerator(),
}
```

## Configuration & Extensibility

### Adding New AWS Services
1. Service is automatically discovered via botocore
2. Parser extracts service definition
3. Generator applies library-specific transformations
4. Templates render the final Python code

### Adding New Target Libraries
1. Create new generator inheriting from `BaseGenerator`
2. Implement library-specific logic
3. Create corresponding Jinja2 templates
4. Register in CLI options

### Customizing Type Generation
Type mappings are configured in `/type_maps/`:
- `shape_type_map.py` - Maps AWS shapes to Python types
- `method_type_map.py` - Override method signatures
- `literal_type_map.py` - Define literal value types

## Performance Considerations

### Template Caching
Templates are cached per process to avoid re-parsing Jinja2:

```python
@lru_cache(maxsize=None)
def get_template(template_path: Path) -> Template:
    return jinja_env.get_template(str(template_path))
```

### Parallel Processing
Services can be processed independently:

```python
# Current: Sequential
for service in services:
    generate_service(service)

# Potential: Parallel
with ThreadPoolExecutor() as executor:
    futures = [executor.submit(generate_service, s) for s in services]
```

### Memory Management
Large service definitions are processed incrementally to manage memory usage.

## Testing Strategy

### Unit Tests
- **Parsers**: Test shape conversion and type mapping
- **Generators**: Test output format correctness
- **Structures**: Test data model consistency

### Integration Tests
- **End-to-end**: Generate complete packages and verify compilability
- **Type checking**: Ensure generated stubs pass mypy/pyright validation
- **Runtime**: Test generated code works with actual AWS services

### Test Data
- Mock AWS service definitions for consistent testing
- Real service samples for integration validation

## Error Handling

### Parsing Errors
- Graceful degradation when service definitions are incomplete
- Detailed error messages with service/shape context
- Fallback to basic types when complex shapes fail

### Generation Errors
- Template rendering failures with clear error context
- Type resolution errors with suggested fixes
- Validation of generated code before output

## CLI Architecture

### Command Structure
```
mypy-boto3-builder
├── generate          # Generate type stubs
├── docs-generate     # Generate documentation
└── chat             # Interactive configuration
```

### Interactive Mode
Uses `questionary` for complex configuration:
- Service selection
- Output format choice
- Custom type mappings

## Future Considerations

### Potential Improvements
1. **Async processing** for faster generation
2. **Incremental builds** to avoid regenerating unchanged services
3. **Plugin system** for custom type transformations
4. **Caching layer** for parsed service definitions

### Scalability
- Current architecture handles 300+ AWS services
- Memory usage scales linearly with service count
- Generation time is dominated by template rendering

## Contributing Guidelines

### Adding Features
1. Start with unit tests for new functionality
2. Update relevant parsers/generators/structures
3. Add templates if new output format is needed
4. Update integration tests
5. Document changes in architecture docs

### Code Style
- Follow existing patterns and naming conventions
- Use type hints for all public APIs
- Add docstrings for complex logic
- Keep functions focused and testable

---

*This architecture supports generating type annotations for 300+ AWS services across multiple Python AWS SDK libraries, enabling static type checking for millions of lines of AWS SDK usage.*