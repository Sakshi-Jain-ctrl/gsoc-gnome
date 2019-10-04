## The Original Project Description:

Create a Django based form to request an account making sure the
account naming policy and other guidelines are taken into account,
automatically mail the module maintainers to receive approval. If
confirmed by module maintainers, land the account name and other
information on a separate page where the accounts team can approve
further. When the approval is given it should make an API call to
FreeIPA and create the account right away.

**Here you go with some details:**

## TODO

1. For account naming policies and guidelines I meant whenever someone
requests a GNOME account it should follow the naming policy as found
at [1], that means the django app should double check whether the
rules have been followed before allowing the username to be used



2. The form should come with the following details: name, surname,
email, ssh public key, requested account name, name of the GNOME
module the person is applying for (each of the projects use a DOAP
file that lists a set of information including maintainers, module
name, bug tracking URL etc. [2], in addition you can also know all the
supported modules by looking at the following file [3])



3. Once the form has been filed in the maintainers of the selected
module(s) should be notified about a pending request. They should be
able to login to the django app and approve / reject the account, once
done the account should be listed on a separate page and marked as
ready to be created. Performing another action (such as clicking a
"Create Account" button) should allow the accounts team to create or
reject the account.



4. The authentication backend will be LDAP. Specifically we're using
FreeIPA which means you should be interacting with the ipa python api
to successfully create the account once it has received all the
approvals



5. The infrastructure where this app is going to run is Openshift
which means you're free to use the latest and greatest Django version
you may see fit



6. The accounts creation process now consists of many manual steps:
applicant submit an account request by mailing accounts@gnome.org, we
receive the request, mail maintainers, wait for maintainer approval,
once received we create the account on IPA manually



7. Module maintainers are GNOME developers working on any of the
projects listed within [4]



Available for any further questions, thanks!




- [1] https://wiki.gnome.org/AccountsTeam/AccountNamePolicy
- [2] https://gitlab.gnome.org/GNOME/gnome-shell/raw/master/gnome-shell.doap
- [3] https://gitlab.gnome.org/repositories.doap
- [4] https://gitlab.gnome.org/GNOME
