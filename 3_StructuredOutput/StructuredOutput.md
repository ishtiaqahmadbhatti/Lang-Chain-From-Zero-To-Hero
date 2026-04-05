Meta Description:  
Learn how to generate structured outputs from LLMs using TypedDict, Pydantic, and JSON Schema for seamless integration with APIs and databases.

Keywords:  
structured output, LLM integration, TypedDict, Pydantic, JSON Schema

Title:  
How to Generate Structured Output from LLMs for System Integration

---

# How to Generate Structured Output from LLMs for System Integration

Language models (LLMs) like ChatGPT have revolutionized natural language processing by interacting with humans through unstructured text. However, when it comes to integrating these models with other systems such as databases or APIs, unstructured outputs pose a significant challenge. In this blog post, we will explore the concept of **structured output** and how it can be leveraged to make LLMs communicate effectively with other software systems. We will also dive into practical implementations using Python tools such as **TypedDict**, **Pydantic**, and **JSON Schema**.

---

## Understanding Unstructured vs Structured Output from LLMs

### What is Unstructured Output?  
When you ask a question to an LLM, it typically responds with plain text. For example, the prompt:

> "What is the capital of India?"

will yield:

> "New Delhi is the capital of India."

This output, although informative, is **unstructured** because it is free-form text without a predefined format or schema. Such outputs are difficult to parse programmatically or integrate with systems that expect data in specific formats.

### What is Structured Output?  
Structured output refers to LLM responses delivered in a well-defined data format such as JSON, dictionaries, or schemas. Instead of a plain text response, the LLM returns data objects with explicit keys and values, for example:

```json
[
  {"time": "morning", "activity": "visit Eiffel Tower"},
  {"time": "afternoon", "activity": "visit museum"},
  {"time": "evening", "activity": "have dinner"}
]
```

This format is predictable, parseable, and can be directly used to store or process information programmatically.

---

## Why Use Structured Output from LLMs?

### Benefits of Structured Output
- **Easy Integration:** Structured data can be seamlessly passed to databases, APIs, or other backend services.
- **Automation:** Enables automation by allowing systems to trigger actions based on specific fields in the output.
- **Data Extraction:** Helps in extracting meaningful data points like summaries, sentiments, names, or ratings from raw text.
- **Building Agents:** Facilitates the creation of intelligent agents that can perform calculations, call tools, or interact with other software components.

### Practical Use Cases
1. **Data Extraction from Resumes:** Extract candidate details such as name, education marks, and previous companies from uploaded resumes and store them in a structured database.
2. **API Development for Reviews:** Parse product reviews, extract pros, cons, sentiment analysis, and topics, and provide this structured data through APIs.
3. **Smart Agents:** Build agents that understand commands in structured form, enabling them to perform precise tool calls like calculating square roots or querying databases.

---

## Generating Structured Output Using `with_structured_output` Function

The **`with_structured_output`** function in LangChain simplifies requesting structured responses from LLMs by specifying data formats like TypedDict, Pydantic models, or JSON Schema. We will explore these three methods in detail.

---

# 1. Using TypedDict for Structured Output

### What is TypedDict?  
`TypedDict` is a Python way to define dictionaries with specific key-value type pairs. It helps ensure that the dictionary keys and their corresponding value types are consistent throughout the codebase.

### Benefits
- Provides type hinting to IDEs.
- Offers basic communication of expected dictionary structure.
- Lightweight and easy to implement.

### Limitations
- No runtime validation — if a wrong data type is passed, it will not raise an error.
- Not suitable for enforcing strict data correctness.

### Example: Defining a TypedDict Schema

```python
from typing import TypedDict

class Review(TypedDict):
    summary: str
    sentiment: str
```

### Generating Structured Output Using TypedDict

```python
from langchain.chat_models import ChatOpenAI

model = ChatOpenAI()

# Use `with_structured_output` to specify TypedDict schema
structured_model = model.with_structured_output(Review)

review_text = "The phone has excellent battery life but the display is average."

result = structured_model.invoke(review_text)
print(result)
# Output: {'summary': '...', 'sentiment': 'positive'}
```

---

# 2. Using Pydantic for Validation and Structured Output

### What is Pydantic?  
Pydantic is a powerful Python library for data validation and settings management using Python type annotations. It parses input data, validates it, and provides helpful error messages if data is invalid.

### Advantages over TypedDict
- **Runtime validation:** Throws errors if data doesn't conform to schema.
- **Default values:** Supports default values for missing fields.
- **Type coercion:** Automatically converts compatible types (e.g., string "32" to int 32).
- **Advanced features:** Supports regex validation, custom constraints, and field descriptions.

### Example: Defining a Pydantic Model

```python
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional, Literal

class Review(BaseModel):
    themes: List[str] = Field(..., description="List of themes discussed in the review")
    summary: str = Field(..., description="Brief summary of the review")
    sentiment: Literal["positive", "negative", "neutral"] = Field(..., description="Overall sentiment")
    pros: Optional[List[str]] = Field(None, description="List of pros mentioned")
    cons: Optional[List[str]] = Field(None, description="List of cons mentioned")
    reviewer_name: Optional[str] = Field(None, description="Name of the reviewer")
```

### Generating Structured Output with Pydantic and LangChain

```python
# Create Pydantic-based structured output model
pydantic_structured_model = model.with_structured_output(Review)

review_text = "Battery lasts long, but the display could be better."

result = pydantic_structured_model.invoke(review_text)
print(result.summary)
print(result.sentiment)
```

### Additional Features of Pydantic with LLMs
- Use field descriptions to guide model prompt generation, reducing ambiguities.
- Validation prevents incorrect data formats such as invalid emails.
- Handles optional fields gracefully.

---

# 3. Using JSON Schema for Cross-Language Compatibility

### What is JSON Schema?  
JSON Schema is a language-independent format for defining the structure and validation rules of JSON data. It is widely used in API design and data interchange.

### Advantages
- Universally supported across multiple programming languages.
- Ideal for projects with multi-language stacks (e.g., Python backend + JavaScript frontend).
- Complements the use of TypedDict and Pydantic when cross-platform data interchange is required.

### Example JSON Schema for Review Data

```json
{
  "title": "Review",
  "type": "object",
  "properties": {
    "themes": {
      "type": "array",
      "items": { "type": "string" },
      "description": "List of themes discussed in the review"
    },
    "summary": {
      "type": "string",
      "description": "Brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["positive", "negative", "neutral"],
      "description": "Overall sentiment of the review"
    },
    "pros": {
      "type": ["array", "null"],
      "items": { "type": "string" },
      "description": "List of pros mentioned"
    },
    "cons": {
      "type": ["array", "null"],
      "items": { "type": "string" },
      "description": "List of cons mentioned"
    },
    "reviewer_name": {
      "type": ["string", "null"],
      "description": "Name of the reviewer"
    }
  },
  "required": ["themes", "summary", "sentiment"]
}
```

### Using JSON Schema with LangChain

```python
from langchain.schema import JsonSchema

json_schema = JsonSchema.from_dict(json_schema_dict)

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke(review_text)
print(result["summary"])
print(result["sentiment"])
```

---

## Choosing the Right Approach: TypedDict vs Pydantic vs JSON Schema

| Criteria                      | TypedDict             | Pydantic                  | JSON Schema                  |
|-------------------------------|-----------------------|---------------------------|------------------------------|
| Language Dependency            | Python only           | Python only               | Language agnostic             |
| Runtime Validation             | No                    | Yes                       | Depends on implementation     |
| Default Values Support         | No                    | Yes                       | Yes                          |
| Type Coercion                 | No                    | Yes                       | No                           |
| Cross-language Compatibility  | No                    | No                        | Yes                          |
| Ease of Use                   | Simple, lightweight   | More complex, powerful    | Requires JSON tools           |

**Recommendations:**
- Use **TypedDict** for lightweight projects entirely in Python without strict validation needs.
- Use **Pydantic** for Python projects with validation, default values, and error handling.
- Use **JSON Schema** for multi-language projects or where universal data interchange is required.

---

## Handling Models That Don’t Support Structured Output Natively

Some open-source or custom LLMs do not support native structured output modes (e.g., JSON or function calling). For these models, you must parse unstructured outputs manually or use **output parsers** to enforce structure programmatically. This is a more advanced topic covered in follow-up resources.

---

## Summary and Best Practices

- Structured output transforms LLMs from text generators into data providers compatible with software systems.
- LangChain’s `with_structured_output` function enables seamless request of structured data from LLMs.
- TypedDict, Pydantic, and JSON Schema provide flexible schema definitions catering to different use cases.
- Incorporate field descriptions and annotations to guide LLMs toward accurate and consistent output.
- Always consider your project’s ecosystem and validation needs when choosing a schema format.
- For LLMs that don’t support structured output natively, plan to implement output parsing or validation layers.

---

## Frequently Asked Questions (FAQ)

### Q1: Can I enforce strict validation on LLM outputs?  
Yes, using **Pydantic** models enables runtime validation and error handling for incoming LLM responses.

### Q2: What if I need to work with front-end JavaScript and back-end Python?  
Use **JSON Schema** as it is language-agnostic and understood across multiple platforms.

### Q3: Does every LLM support structured output?  
No, some models (especially open-source ones like TinyLlama) do not support structured output natively, requiring manual parsing.

### Q4: How can I improve the accuracy of structured outputs?  
Provide detailed field descriptions and annotations (annotations) in your schema, helping the LLM understand output expectations.

---

Harnessing structured output capability from LLMs unlocks a new dimension of AI integration, making your applications smarter, more reliable, and easier to maintain. Whether you are building chatbots, data extraction tools, or intelligent agents, mastering these techniques will set you apart in the rapidly evolving AI landscape.

Happy coding!