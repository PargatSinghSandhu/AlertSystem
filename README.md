Monitoring and alert system for Baru Sahib

Problem: Thousands of cheques submitted to Baru Sahib, but the records of that, are the 
cheques submitted on time taken care manually, which create the discrepancies. So to 
remove this I'm building a automated monitoring and alert system.

This system will track all the cheques.
Approach:
1. Fetch all the details of the cheque.
2. The system will check that if the cheque is not submitted on time.
3. Now based on the missed date, if that is the first day, it will raise Yellow Alert, 
by sending an email.
4. If 2 days have passed then it will send an email with orange alert
5. If 3 days have passed, it will send an email with red alert.

Repository: https://github.com/PargatSinghSandhu/AlertSystem.git
