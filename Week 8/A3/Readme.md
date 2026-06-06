🏗️ System Architecture & Development ProcessInstead of standard single-label cross-entropy, this architecture forks the hidden representations after a shared feature-extraction backbone to drive two parallel classifier heads.                  

                 [ Input Image (3x32x32) ]
                              │
                    [ Shared CNN Backbone ]
                              │
               ┌──────────────┴──────────────┐
               ▼                             ▼
     [ Superclass Head ]           [ Subclass Head ]
       (Output: 2 Logits)           (Output: 10 Logits)
     Animals vs. Transport          Fine-Grained Classes

     
1. Hierarchical Class Mapping
   The standard 10 classes of CIFAR-10 were partitioned into 2 meaningful Superclasses:

Superclass 0 (Objects / Transport): airplane, automobile, ship, truck
Superclass 1 (Living Things / Animals): bird, cat, deer, dog, frog, horse2. 

2. Multi-Task Joint Loss
   Optimization is performed concurrently across both taxonomies by minimizing a weighted joint Multi-Task Cross-Entropy loss:
   
<img width="678" height="140" alt="Screenshot 2026-06-06 at 9 00 38 PM" src="https://github.com/user-attachments/assets/f9e908bd-7571-412f-ad8a-b34a3f2b5031" />


   💻 Getting Started
   
   PrerequisitesEnsure you have Python 3.8+ and standard PyTorch dependencies installed.

 <img width="810" height="152" alt="Screenshot 2026-06-06 at 9 05 40 PM" src="https://github.com/user-attachments/assets/57125a38-4a92-46f6-8e26-faacfae3be8c" />

   
Training the Multi-Level Network

To run the training loop, configure your weights, and execute evaluations:

<img width="829" height="158" alt="Screenshot 2026-06-06 at 9 04 31 PM" src="https://github.com/user-attachments/assets/31c2add2-f036-4667-a858-32c3391e94e8" />


📊 Detailed Metrics
<img width="767" height="184" alt="Screenshot 2026-06-06 at 9 02 53 PM" src="https://github.com/user-attachments/assets/62d1911c-3daa-428a-8841-3c8490779c07" />


🔗 Project Context

This framework was adapted and extended from the baseline CIFAR-10 pipelines to support advanced hierarchical visual taxonomies.
Main Repository URL: github.com/dev-architect/cifar10-multilevel-classification

**Output trained model is:** CIFAR_10_tens.h5


