#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Tie
%define		pnam	TwoLevelHash
%include	/usr/lib/rpm/macros.perl
Summary:	Tie::TwoLevelHash - tied interface to multi-dimensional (two-level) hash files
Summary(pl.UTF-8):	Tie::TwoLevelHash - interfejs do wielowymiarowych (dwupoziomowych) plików haszy
Name:		perl-Tie-TwoLevelHash
Version:	1.2
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	68cb91a69c63ef90018e7395948fa828
URL:		http://search.cpan.org/dist/Tie-TwoLevelHash/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Tie::TwoLevelHash module. It is a TIEHASH interface which
lets you tie to a text file which is a multi-dimensional (two level)
hash.

%description -l pl.UTF-8
To jest moduł Tie::TwoLevelHash. Jest to interfejs TIEHASH, który
pozwala dowiązać się do pliku tekstowego, który jest wielowymiarowym
(dwupoziomowym) haszem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Tie/TwoLevelHash.pm
%{_mandir}/man3/*
