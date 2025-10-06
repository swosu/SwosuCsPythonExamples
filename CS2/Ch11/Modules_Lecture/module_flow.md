# Python Module Import Flow

```mermaid
flowchart TD
    A[funcs.py\nDefines fct() and sq()]:::module
    B[script1.py\nImports funcs.py\nUses fct()*sq()]:::script
    C[script2.py\nImports funcs.py\nUses fct()/sq()]:::script
    D[master_script.py\nImports funcs.py\nImports script1 & script2\nDemonstrates all together]:::main

    A --> B
    A --> C
    A --> D
    B --> D
    C --> D

classDef module fill:#2b90d9,stroke:#0f3b57,color:#fff,stroke-width:2px;
classDef script fill:#a1c4fd,stroke:#0f3b57,color:#000;
classDef main fill:#ffcc70,stroke:#cc9900,color:#000;

