# Selinux
Selinux defines access controls for the application, processes, and files on a system.
It uses security policies, which are a set of rules that tell Selinux what can or can't be accessed, to enforce the access allowed by a policy.

When an application or process, known as a subject, makes a request to access an object, like a file, SeLinux checks with an access vector cache (AVC), were permissions are chached for subjects and objects.
> process나 app이 특정한 access를 할 때 SELinux는 AVC(Access Vector cache)를 통해 권한을 확인한다.


If Selinux is unable to make a decision about access based on the cached permissions, it sends the request to the security server.
The security server checks for the security context of the app or process and the file.
Security context is applied from the SELinux policy database. Permission is then granted or denied.
> 접근 권한에 대한 내용 결정을 내리지 못하는 경우 security server로 가서 이를 확인한다.

If permission is denied, an "avc: denied" message will be available in /var/log.messages.
> 권한이 부여되지 못한 경우 /var/log.messages 에 log를 남긴다.


## Reference
- [Reference](https://www.redhat.com/en/topics/linux/what-is-selinux)