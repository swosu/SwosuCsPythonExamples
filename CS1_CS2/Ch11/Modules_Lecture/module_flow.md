# Python Module Import Flow

```mermaid
flowchart TD
    A[funcs.py - defines fct() and sq()]:::module
    B[script1.py - imports funcs.py and uses fct()*sq()]:::script
    C[script2.py - imports funcs.py and uses fct()/sq()]:::script
    D[master_script.py - imports funcs.py, script1, and script2]:::main

    A --> B
    A --> C
    A --> D
    B --> D
    C --> D

classDef module fill:#2b90d9,stroke:#0f3b57,color:#fff,stroke-width:2px;
classDef script fill:#a1c4fd,stroke:#0f3b57,color:#000;
classDef main fill:#ffcc70,stroke:#cc9900,color:#000;

