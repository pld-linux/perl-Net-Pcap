#
# Conditional build:
%bcond_with	tests	# perform "make test" (require root privilleges)
#
%define		pdir	Net
%define		pnam	Pcap
Summary:	Net::Pcap - Perl binding to the LBL pcap(3) packet capture library
Summary(pl.UTF-8):	Net::Pcap - dowiązanie Perla do biblioteki przechwytywania pakietów LBL pcap(3)
Name:		perl-Net-Pcap
Version:	0.21
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b0eb2495d1f7e720146bb3feac1e605e
Patch0:		%{name}-perl_settings.patch
URL:		http://search.cpan.org/dist/Net-Pcap/
BuildRequires:	libpcap-devel >= 1.9.0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::Pcap module is a Perl binding to the LBL pcap(3) packet
capture library.

%description -l pl.UTF-8
Moduł Net::Pcap jest dowiązaniem Perla do biblioteki przechwytywania
pakietów LBL pcap(3).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	CCFLAGS="%{rpmcflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64" \
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
%doc Changes README
%attr(755,root,root) %{_bindir}/pcapinfo
%{perl_vendorarch}/Net/Pcap.pm
%dir %{perl_vendorarch}/auto/Net/Pcap
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Pcap/Pcap.so
%{_mandir}/man1/pcapinfo.1p*
%{_mandir}/man3/Net::Pcap.3pm*
