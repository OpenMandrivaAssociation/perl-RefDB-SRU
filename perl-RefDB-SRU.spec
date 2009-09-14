%define module	RefDB-SRU
%define name	perl-%{module}
%define version 0.7
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPLv2+
Group:		Development/Perl
URL:		http://refdb.sourceforge.net
Source:		http://prdownloads.sourceforge.net/refdb/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Perl component for the MARC and Pubmed import filters.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
# tests require a RefDB server
#%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog
%{perl_vendorlib}/RefDB
%{_mandir}/*/*

