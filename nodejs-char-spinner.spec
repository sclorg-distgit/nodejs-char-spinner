%{?scl:%scl_package nodejs-char-spinner}
%{!?scl:%global pkg_name %{name}}

%nodejs_find_provides_and_requires
Name:           %{?scl_prefix}nodejs-char-spinner
Version:        1.0.1
Release:        2%{?dist}
Summary:        Node.js char spinner
License:        ISC
Group:          Development/Languages/Other
Url:            https://github.com/isaacs/char-spinner
Source:         http://registry.npmjs.org/char-spinner/-/char-spinner-%{version}.tgz
BuildRequires:  %{scl}
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-build
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

%description
Put a little spinner on process.stderr, as unobtrusively as possible. 

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/char-spinner
cp -pr package.json spin.js \
        %{buildroot}%{nodejs_sitelib}/char-spinner

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{nodejs_sitelib}/char-spinner

%changelog
* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-2
- Remove undefined macro

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-1
- Initial build

