%include	/usr/lib/rpm/macros.perl
%define         pdir Net
%define         pnam Pcap

Summary:	Perl binding to the LBL pcap(3) packet capture library
Summary(pl):	Dowi�zanie perla do biblioteki przechwytywania pakiet�w LBL pcap(3)
Name:		perl-%{pdir}-%{pnam}
Version:	0.04
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::Pcap module is a Perl binding to the LBL pcap(3) packet
capture library.

%description -l pl
Modu� Net::Pcap jest dowi�zaniem perla do biblioteki przechwytywania
pakiet�w LBL pcap(3).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
gzip -9nf README 
find $RPM_BUILD_ROOT -name .packlist | xargs -r rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/%{pdir}/%{pnam}.pm
%{perl_sitearch}/auto/%{pdir}/%{pnam}
%{_mandir}/man3/*
%doc *.gz
