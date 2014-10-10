%define module	RefDB-SRU

Name:		perl-%{module}
Version:	0.7
Release:	4
Summary:	%{module} module for perl
License:	GPLv2+
Group:		Development/Perl
URL:		http://refdb.sourceforge.net
Source:		http://prdownloads.sourceforge.net/refdb/%{module}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Perl component for the MARC and Pubmed import filters.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
# tests require a RefDB server
#make test

%install
%makeinstall_std

%files
%doc ChangeLog
%{perl_vendorlib}/RefDB
%{_mandir}/*/*



%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.7-2mdv2010.0
+ Revision: 440620
- rebuild

* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.7-1mdv2009.1
+ Revision: 355064
- import perl-RefDB-SRU


* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.7-1mdv2009.1
- first release
