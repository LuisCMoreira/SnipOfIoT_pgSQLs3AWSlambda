# SnipOfIoT_pgSQLs3AWSlambda

### Requirement Summary:

- Lambda funtion is to be setup in the same VPC (and security group) as the PostgreSQL host.

- In the AWS VPC Managment Console: Creaty an endpoint:
  * AWS service
  * com.amazonaws.<region code>.s3
  * Type: Gateway
  * Same VPC of the Lambda Function and the PostgresSQL host.

- In the inbound Rules of the security group, setup a rule with: TCP port of PostgreSQL (default=5432) is open to the same security group.

- Disclaimer: In the outbound Rules of the security group, setup was already for an application requiring all trafic available to any IP.
