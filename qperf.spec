Name:           qperf
Summary:        Measure socket and RDMA performance
Version:        0.4.9
Release:        1
License:        BSD 3-Clause, GPL v2
Group:          Networking/Diagnostic
Source:         http://www.openfabrics.org/downloads/qperf/%{name}-%{version}.tar.gz
Url:            http://www.openfabrics.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#BuildRequires:  libibverbs-devel
#BuildRequires:  librdmacm-devel

%description
Measure socket and RDMA performance.

%prep
%setup -q

%build
%configure
export CFLAGS="$RPM_OPT_FLAGS"
%{__make}

%install
install -D -m 0755 src/qperf $RPM_BUILD_ROOT%{_bindir}/qperf
install -D -m 0644 src/qperf.1 $RPM_BUILD_ROOT%{_mandir}/man1/qperf.1

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-, root, root)
%doc COPYING
%_bindir/qperf
%_mandir/man1/qperf.1*

%changelog
* Sat Oct 20 2007 - johann@georgex.org
- Initial package
