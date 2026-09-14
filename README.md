# BuildPulse Demo Services

Synthetic microservices and engineering metadata for the BuildPulse AI hackathon demo. This repository contains no production code, customer data, credentials, or real employee information.

| Service | Team | Primary owner | Backup | Dependencies |
| --- | --- | --- | --- | --- |
| Loan Service | Lending Platform | Meera Kulkarni | Arjun Rao | Payments API, Identity Service |
| Payments API | Payments Platform | Dev Shah | Kavya Thomas | API Gateway |
| API Gateway | Developer Platform | Jose Nair | Priya Menon | Identity Service |
| Identity Service | Core Services | Sandeep Batra | Nisha Kapoor | — |

BuildPulse uses `service-catalog.yaml` as the source of truth for service ownership and dependencies. Contribution history is only an ownership-confidence signal.

BuildPulse reads this repository as a **read-only intelligence source**. It never executes the service code.
