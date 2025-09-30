\documentclass[12pt]{article}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{geometry}
\geometry{margin=1in}
\usepackage{enumitem}
\usepackage{tikz}

\title{Worksheet: The Sieve of Eratosthenes}
\author{}
\date{}

\begin{document}
\maketitle

\section*{Introduction}
The \textbf{Sieve of Eratosthenes} is a classic method for finding all prime numbers up to a specified integer.  
\begin{itemize}
    \item \textbf{Pronunciation:} ``Eratosthenes'' is pronounced \emph{Air-uh-TOSS-thuh-neez}.
    \item Eratosthenes (276--194 B.C.E.) was a Greek scholar known for his work in mathematics, geography, and astronomy.  
\end{itemize}

\section*{Step-by-Step Examples}

\subsection*{Example 1: Small Case (Find primes $\leq 10$)}
\begin{enumerate}
    \item Write numbers $2$ through $10$: 2, 3, 4, 5, 6, 7, 8, 9, 10.
    \item Start with $2$. Cross out multiples of $2$: 4, 6, 8, 10.
    \item Next available number is $3$. Cross out multiples of $3$: 9.
    \item Remaining numbers: 2, 3, 5, 7. These are primes $\leq 10$.
\end{enumerate}

\subsection*{Example 2: Medium Case (Find primes $\leq 30$)}
\begin{enumerate}
    \item Begin: 2, 3, 4, 5, 6, 7, \dots, 30.
    \item Strike out multiples of $2$: 4, 6, 8, 10, \dots, 30.
    \item Next available is $3$. Strike out multiples: 6, 9, 12, 15, \dots, 30.
    \item Next available is $5$. Strike out multiples: 10, 15, 20, 25, 30.
    \item Next available is $7$. Multiples beyond 30 exceed the limit.
    \item Remaining: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
\end{enumerate}

\subsection*{Example 3: Larger Case (Find primes $\leq 100$)}
We now extend the sieve to 100. Notice this version shows more detail than the textbook:
\begin{enumerate}[label=Step \arabic*:]
    \item Write numbers 2--100.
    \item Cross out multiples of $2$: 4, 6, 8, \dots, 100.
    \item Next prime is $3$. Cross out multiples: 9, 12, 15, \dots, 99.
    \item Next prime is $5$. Cross out multiples: 25, 30, 35, \dots, 100.
    \item Next prime is $7$. Cross out multiples: 49, 56, 63, \dots, 98.
    \item Next prime is $11$. Since $11^2 = 121 > 100$, the sieve stops here.
    \item Remaining uncrossed numbers are primes up to 100.
\end{enumerate}

\section*{Pseudocode for the Sieve}
\begin{verbatim}
function sieve(n):
    create a list isPrime[2..n] initialized to true
    for p from 2 to sqrt(n):
        if isPrime[p]:
            for multiple from p*p to n step p:
                isPrime[multiple] = false
    return all numbers i where isPrime[i] = true
\end{verbatim}

\section*{Extension: Prime Gaps and Predictions}
We can use the sieve to study the \emph{spacing} between consecutive prime numbers.

\subsection*{Step 1: Generate primes up to 1000}
Use the sieve function to collect all primes $\leq 1000$.  

\subsection*{Step 2: Calculate prime gaps}
Let $p_k$ be the $k$th prime. Define the \emph{prime gap} $g_k = p_{k+1} - p_k$.  
Compute $g_1, g_2, g_3, \dots$ up to 1000.

\subsection*{Step 3: Make a simple prediction}
Based on the last few gaps, predict the distance from the largest prime found ($p_m$) to the next prime.  
For example: use the average of the last 5 gaps.

\subsection*{Step 4: Test the prediction}
Run the sieve up to $p_m + 200$ and find the actual next prime(s).  
Compare predicted prime positions with the actual values.

\section*{Outline of Python-Style Code}

\subsubsection*{Sieve Implementation}
\begin{verbatim}
def sieve(n):
    primes = []
    isPrime = [True] * (n+1)
    isPrime[0] = isPrime[1] = False
    for p in range(2, int(n**0.5)+1):
        if isPrime[p]:
            for multiple in range(p*p, n+1, p):
                isPrime[multiple] = False
    for i in range(2, n+1):
        if isPrime[i]:
            primes.append(i)
    return primes
\end{verbatim}

\subsubsection*{Prime Gap and Prediction}
\begin{verbatim}
def prime_gaps(primes):
    gaps = []
    for i in range(len(primes)-1):
        gaps.append(primes[i+1] - primes[i])
    return gaps

# Simple prediction: average of last few gaps
def predict_next(primes, gaps):
    avg_gap = sum(gaps[-5:]) / 5
    last_prime = primes[-1]
    predicted = last_prime + round(avg_gap)
    return predicted
\end{verbatim}

\section*{Student Task}
\begin{enumerate}
    \item Work through the sieve manually for $n=10$, $n=30$, and $n=100$.
    \item Write pseudocode for the sieve in your own words.
    \item Use the given code outline to implement the sieve in Python.
    \item Compute prime gaps up to 1000.
    \item Make a prediction for the next prime after 1000 and test your prediction.
\end{enumerate}

\end{document}
