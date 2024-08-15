---
layout: post
title: 计算机与通信系统性能分析总结
date: 2022-3-30
tags: 计算机理论
---

# 开放系统&封闭系统
在计算机系统的性能分析中，开放系统和封闭系统是两种不同的系统模型，它们在资源使用和用户交互方面有显著的区别。

### 开放系统 (Open System)
开放系统是指那些可以与外界进行交互，并且其用户和任务数目可以随时间变化的系统。具体特点包括：

1. **动态用户/任务数量**：用户和任务可以在任何时间进入或离开系统。系统的负载因此是不确定的。
2. **无限用户来源**：用户请求可以来自于系统外部，无限制地增加。
3. **请求到达率**：系统的负载通常由到达率（arrival rate）来描述，即单位时间内新请求到达系统的速率。
4. **典型应用**：Web服务器、电子邮件系统、在线交易系统等，这些系统需要处理来自外部的连续请求。

### 封闭系统 (Closed System)
封闭系统是指那些系统内部用户和任务数目是固定的，资源循环使用，用户和任务不会随时间变化。具体特点包括：

1. **固定用户/任务数量**：用户和任务的数目在分析期间是固定的，只有当某个任务完成后，新的任务才会进入系统。
2. **有限用户来源**：系统的负载是由一组固定的用户生成的。
3. **循环负载**：任务完成后，用户会产生新的任务，继续占用系统资源。
4. **响应时间**：系统性能通常通过用户响应时间来衡量，系统内部用户的等待时间和服务时间影响整体性能。
5. **典型应用**：批处理系统、内部计算任务等，这些系统任务数目不变，资源循环使用。

### 比较
- **负载特性**：开放系统的负载是不确定的，可以随时增加；而封闭系统的负载是固定的，基于系统内部用户生成的任务。
- **性能指标**：开放系统通常关注到达率和吞吐量；封闭系统则关注响应时间和用户等待时间。

# 常见概率分布
### 1. **均匀分布 (Uniform Distribution)**：
   - 概率密度函数 (PDF)：$$f(x) = \begin{cases}
     \frac{1}{b - a} & \text{if } a \leq x \leq b \\
     0 & \text{otherwise}
     \end{cases} $$
   - 其中，$a$ 和 $b$ 是分布的上下界限。

### 2. **正态分布 (Normal Distribution)**：
   - 概率密度函数 (PDF)：$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} $$
   - 其中，$\mu$ 是均值，$\sigma$ 是标准差。

### 3. **指数分布 (Exponential Distribution)**：
   - 概率密度函数 (PDF)：$$f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$$
   - 其中，$\lambda$ 是分布的参数，通常表示为速率参数或者尺度参数。

### 4. **泊松分布 (Poisson Distribution)**：
   - 概率质量函数 (PMF)：$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \ldots$$
   - 其中，$\lambda$ 是平均事件发生率。

### 5. **二项分布 (Binomial Distribution)**：
   - 概率质量函数 (PMF)：$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, 2, \ldots, n $$
   - 其中，$n$ 是试验次数，$p$ 是每次试验成功的概率。
   - $$\binom{n}{k}={n!\over k!(n-k)!}$$
   - 在n个位置中选k个

![](/images/2024-08-15-xingnengfenxi\Pastedimage20240613143947.png)

# 基本操作
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240710151321.png)

![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703144826.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703144855.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703144949.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703145011.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703145043.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703145204.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703145651.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240710152551.png)
	**Throughput: X~jobs/sec**
	**The total service demand on device i: $D_i$~sec/jobs**
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240710152614.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240710152636.png)

# DTMC
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703150530.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703151246.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703151259.png)、
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703151041.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703152307.png)
**这不就是特征向量**
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703152506.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703152640.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703153141.png)
这个公式表示一个无穷级数的求和公式。公式的具体形式如下：
$$\sum_{i=0}^{\infty} i b^i = \frac{b}{(1-b)^2} $$
其中，$b$ 是一个常数，满足 $|b| < 1$。
解释如下：
1. **左侧：** $\sum_{i=0}^{\infty} i b^i$
   - 这是一个从 $i = 0$ 到 $i = \infty$ 的无穷级数。
   - 每项的形式是 $i b^i$，即 $i$ 乘以 $b$ 的 $i$ 次幂。
2. **右侧：** $\frac{b}{(1-b)^2}$
   - 这是该无穷级数的和。
   - 右侧的分数形式是  $\frac{b}{(1-b)^2}$，表示在满足 $|b| < 1$ 的条件下，无穷级数的总和。
**推导过程：**
1. 我们知道几何级数的求和公式：$\sum_{i=0}^{\infty} b^i = \frac{1}{1-b}$
2. 将上面的公式对 $b$ 求导，得到：$\sum_{i=0}^{\infty} i b^{i-1} = \frac{1}{(1-b)^2}$
3. 再乘以 $b$，得到：$\sum_{i=0}^{\infty} i b^i = \frac{b}{(1-b)^2}$

# CTMC
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703161517.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703161531.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703161748.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703161737.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703162832.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703162908.png)


![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703171821.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703171957.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703172045.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703172502.png)
 **条件 $\pi_j \nu_j = \sum_i \pi_i q_{ij}$：** 
   - $\nu_j$ 是状态 $j$ 的离开速率（即状态 $j$ 的总离开率）。
   - $q_{ij}$ 是从状态 $i$ 到状态 $j$ 的过渡速率。
   - 该条件表示状态 $j$ 的稳态概率乘以其离开速率等于所有状态 $i$ 的稳态概率乘以从状态 $i$ 到状态 $j$ 的过渡速率之和。简单来说，这是平衡方程的一种形式，表示在稳态下进入和离开状态 $j$ 的速率是相等的。

# M/M/1
- The  “M” in this first slot stands for “memoryless” and says that the interarrival times are Exponentially distributed. 
- The second slot characterizes the distribution of the service  times. The “M” in this slot says that the service times of jobs are “memoryless,” namely  Exponentially distributed. 
- The third slot indicates the number of servers in the system.  For now this is 1, but we will see more complicated examples later. 
- A fourth slot is  typically used to indicate an upper bound on the capacity of the system in terms of  the total space available to hold jobs. Sometimes, however, the fourth slot is used to indicate the scheduling discipline used for the system. The absence of a fourth field  indicates that the queue is unbounded and that the scheduling policy is FCFS.
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703183745.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703190253.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240717203549.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240717203607.png)
The mean number of customers in the system: 
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240717203624.png)![](/images/2024-08-15-xingnengfenxi\Pastedimage20240717203642.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240717203704.png)
- We’ll assume an ergodic continuous-time system. 
- Let $π_n = p_n$ be the limiting probability that there are n jobs in the system (or equivalently the long-run fraction of time that there are n jobs in the system). 
- Let $a_n$ be the limiting probability that an arrival sees n jobs in the system (or equivalently the long-run fraction of arrivals that see n jobs). 
- Let $d_n$ be the limiting probability that a departure leaves behind n jobs in the system when it departs (or equivalently the long-run fraction of departures that leave behind n jobs).
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703190306.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703190318.png)
PASTA – “Poisson Arrivals See Time Averages”
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240703190329.png)

![](/images/2024-08-15-xingnengfenxi\Pastedimage20240704113957.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240704114015.png)
最可能用到：
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240704133445.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240704133829.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240704133844.png)
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240704133913.png)
Number of Jobs in Queue:
![](/images/2024-08-15-xingnengfenxi\Pastedimage20240718140432.png)

![](/images/2024-08-15-xingnengfenxi\Pastedimage20240718141521.png)
