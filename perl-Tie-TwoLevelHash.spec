%include	/usr/lib/rpm/macros.perl
Summary:	Tie-TwoLevelHash perl module
Summary(pl):	Modu³ perla Tie-TwoLevelHash
Name:		perl-Tie-TwoLevelHash
Version:	1.2
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tie/Tie-TwoLevelHash-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-TwoLevelHash perl module.

%description -l pl
Modu³ perla Tie-TwoLevelHash.

%prep
%setup -q -n Tie-TwoLevelHash-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Tie/TwoLevelHash.pm
%{_mandir}/man3/*
