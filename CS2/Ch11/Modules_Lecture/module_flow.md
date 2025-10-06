# Python Module Import Flow

```mermaid
flowchart TD
    A[funcs.py<br/>Defines fct() and sq()]:::module
    B[script1.py<br/>Imports funcs.py<br/>Uses fct()*sq()]:::script
    C[script2.py<br/>Imports funcs.py<br/>Uses fct()/sq()]:::script
    D[master_script.py<br/>Imports funcs.py<br/>Imports script1 & script2<br/>Demonstrates all together]:::main

    A --> B
    A --> C
    A --> D
    B --> D
    C --> D

classDef module fill:#2b90d9,stroke:#0f3b57,color:#fff,stroke-width:2px;
classDef script fill:#a1c4fd,stroke:#0f3b57,color:#000;
classDef main fill:#ffcc70,stroke:#cc9900,color:#000;

