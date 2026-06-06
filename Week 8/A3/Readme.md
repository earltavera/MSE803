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

****Output trained model is:**** CIFAR_10_tens.h5


****Step-by-step breakdown and description of the image classification pipeline built with TensorFlow/Keras to classify the CIFAR-10 dataset.****
============
<img width="811" height="294" alt="Screenshot 2026-06-06 at 11 28 18 PM" src="https://github.com/user-attachments/assets/c7f4049f-9b80-4a74-9e6c-0feb94a02e91" />
<img width="827" height="465" alt="Screenshot 2026-06-06 at 11 29 11 PM" src="https://github.com/user-attachments/assets/d0cbf321-b175-499b-9976-556e2cb4dd19" />
<img width="665" height="540" alt="Screenshot 2026-06-06 at 11 29 48 PM" src="https://github.com/user-attachments/assets/85cc89f5-17f5-40d8-ae66-69ce0a1f41ad" />
<img width="807" height="250" alt="Screenshot 2026-06-06 at 11 30 15 PM" src="https://github.com/user-attachments/assets/4c575f80-64ef-42d3-a52e-71c3d1e4609c" />
<img width="826" height="410" alt="Screenshot 2026-06-06 at 11 30 38 PM" src="https://github.com/user-attachments/assets/951d1736-e282-44fd-aa86-97c6966d3865" />
<img width="848" height="541" alt="Screenshot 2026-06-06 at 11 30 56 PM" src="https://github.com/user-attachments/assets/fb4fd13b-2b13-4446-b9df-83535f9b32fe" />
<img width="768" height="110" alt="Screenshot 2026-06-06 at 11 31 41 PM" src="https://github.com/user-attachments/assets/da14b889-ea2a-4752-8c99-ef165bb36b40" />







