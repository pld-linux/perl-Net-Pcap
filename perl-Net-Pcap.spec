%include	/usr/lib/rpm/macros.perl
%define         pdir Net
%define         pnam Pcap

Summary:	Perl binding to the LBL pcap(3) packet capture library
Summary(pl):	Dowi±zanie perla do biblioteki przechwytywania pakietów LBL pcap(3)
Name:		perl-%{pdir}-%{pnam}
Version:	0.04
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::Pcap module is a Perl binding to the LBL pcap(3) packet
capture library.

%description -l pl
Modu³ Net::Pcap jest dowi±zaniem perla do biblioteki przechwytywania
pakietów LBL pcap(3).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name .packlist | xargs -r rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/%{pdir}/%{pnam}.pm
%{perl_vendorarch}/auto/%{pdir}/%{pnam}
%{_mandir}/man3/*
