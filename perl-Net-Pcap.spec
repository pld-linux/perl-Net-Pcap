#
# Conditional build:
%bcond_with	tests	# perform "make test" (require root privilleges)
#
%include	/usr/lib/rpm/macros.perl
%define         pdir Net
%define         pnam Pcap

Summary:	Net::Pcap - Perl binding to the LBL pcap(3) packet capture library
Summary(pl):	Net::Pcap - dowi±zanie Perla do biblioteki przechwytywania pakietów LBL pcap(3)
Name:		perl-%{pdir}-%{pnam}
Version:	0.04
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3456934b09598122fea6a553cdf42a91
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::Pcap module is a Perl binding to the LBL pcap(3) packet
capture library.

%description -l pl
Modu³ Net::Pcap jest dowi±zaniem Perla do biblioteki przechwytywania
pakietów LBL pcap(3).

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
find $RPM_BUILD_ROOT -name .packlist | xargs -r rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/%{pdir}/%{pnam}.pm
%{perl_vendorarch}/auto/%{pdir}/%{pnam}
%{_mandir}/man3/*
