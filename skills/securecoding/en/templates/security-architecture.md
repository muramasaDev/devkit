# Security Design

- Project:
- Date written:
- Basis: `references/architecture.md` of the `securecoding` skill (`../../references/architecture.md`, Korean for now)
- Leave unknown cells as `미정` (undecided)

## 1. Roles and resources
| Role | Resources and operations accessed | Notes |
|---|---|---|
| Not logged in | | |
| Regular user | | |
| Admin | | |

## 2. Path classes
| Class | Path | Authorization location (one place in the entry layer) |
|---|---|---|
| Public | | |
| Login required | | |
| Admin only | | |

Admin area (if any):
- Additional authentication method:
- Access restriction (IP, network):
- Exposed to the internet:

## 3. Where values are computed (when amounts, stock, or coupons exist)
| Value | Computation location | Duplicate and concurrent request prevention |
|---|---|---|
| Price and total | Server, based on DB values | |
| Stock | | |
| Coupons and one-time benefits | | |
| Payment confirmation | Gateway API and signature verification | |

## 4. Secret storage and keys allowed to be public
Secrets (values used only on the server):
| Secret | Storage location | Owner (update on departure or role change) | Environment split (dev, staging, production) | Rotation period |
|---|---|---|---|---|
| | | | | |

Keys allowed to be public (keys that may be in the browser bundle. Examples: Supabase anon key, Firebase web key):
| Key | Why it is safe to expose | Control this key relies on (e.g., RLS, security rules, domain restriction) | Control location | Control tested |
|---|---|---|---|---|
| | | | | |

A key that appears in the browser bundle but is not in the public-allowed key list is treated as a secret exposure.

## 5. Defaults for verification code, password, and session (if any)
The project decides the values. For defaults, see SEC-02, SEC-06, SEC-10 in `../../references/controls.md` (Korean for now). The number next to each cell is the OWASP ASVS 5.0 requirement number.
| Item | ASVS 5.0 | Value |
|---|---|---|
| Minimum password length | 6.2.1 | |
| Maximum allowed password length | 6.2.9 | |
| Authentication attempt limit (login) | 6.1.1, 6.3.1 | |
| Login failure time window, block duration, IP limit | 6.1.1, 6.3.1 | |
| Password policy basis (KISA or ASVS 5.0, exception approval) | 6.2.1 ~ 6.2.12 | |
| Session idle expiry | 7.1.1, 7.3.1 | |
| Session absolute expiry | 7.1.1, 7.3.2 | |
| Verification code (OTP) length | 6.5.4 | |
| Verification code (OTP) expiry time | 6.5.5 | |
| Verification code attempt limit | 6.6.3 | |
| Delivery method | | |

## 6. AI feature (if any)
| Tools the model can call | Permission required | Human approval required |
|---|---|---|
| | | |

## 7. Data access
- DB access subject:
- Access path (via app server / direct from client):
- If direct access, location of row-level rules:

## Change log
| Date | Change | Reason |
|---|---|---|
| | | |
