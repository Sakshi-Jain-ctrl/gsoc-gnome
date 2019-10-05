from django import forms


# Account Name Requirements

# 1.  The account name needs to be only lowercase letters a-z
# 2.  The account name should also be easily connectable to
#     the full name. This means that the name should be a combination of your first, last,
#     and possibly middle names, or abbreviations or initials of such.
# 3.  If your first and last names are long enough to make the above difficult,
#     we may entertain proposals that are abbreviations of only your first or last name,
#     assuming that they are sufficiently uncommon.
# 4.  Finally, if you already have a gnome.org account, such as a Git account, shell account,
#     or a mail alias, your requested account name needs to be identical to your already existing gnome.org
#     account name (this does not apply for l10n.gnome.org accounts though). In other words, you will have the same
#     account name also for this account. However, in case your existing gnome.org account name does not fulfill the above rules,
#     you may have your gnome.org account name changed, should you want so.


class NameForm(forms.Form):
	your_name = forms.CharField(label='account_name', max_length=10)