Name: libtdb
Version: 1.4.7
Release: 1
Summary: The Tdb library
License: LGPLv3+
URL: http://tdb.samba.org/
Source: http://samba.org/ftp/tdb/tdb-%{version}.tar.gz

BuildRequires: gcc libxslt docbook-style-xsl
BuildRequires: python3-devel
Provides: bundled(libreplace)
Obsoletes: python2-tdb < 1.4.2-1
Obsoletes: python2-samba

%description
Tdb library implements a trivial database.

%package -n tdb-tools
Summary: Developer tools for the Tdb library
Requires: libtdb = %{version}-%{release}

%description -n tdb-tools
Tools to manage Tdb files

%package -n python3-tdb
Summary: Python3 bindings for the Tdb library
Requires: libtdb = %{version}-%{release}
%{?python_provide:%python_provide python3-tdb}

%description -n python3-tdb
Python3 bindings for the Tdb library

%package devel
Summary: Header files for Tdb library
Requires: libtdb = %{version}-%{release}

%description devel
Header files of the Tdb library to develop programs.

%package help
BuildArch: noarch
Summary: Document for the Tdb library

%description help
Document for the Tdb library

%prep
%autosetup -n tdb-%{version} -p1

%build
%configure --disable-rpath \
           --bundled-libraries=NONE \
           --builtin-libraries=replace

%make_build

%check
make %{?_smp_mflags} check

%install
%make_install

%files
%{_libdir}/libtdb.so.*

%files -n tdb-tools
%{_bindir}/tdbbackup
%{_bindir}/tdbdump
%{_bindir}/tdbtool
%{_bindir}/tdbrestore

%files -n python3-tdb
%{python3_sitearch}

%files devel
%{_includedir}/tdb.h
%{_libdir}/libtdb.so
%{_libdir}/pkgconfig/tdb.pc

%files help
%doc docs/README
%{_mandir}/man8/tdbbackup.8*
%{_mandir}/man8/tdbdump.8*
%{_mandir}/man8/tdbtool.8*
%{_mandir}/man8/tdbrestore.8*

%ldconfig_scriptlets

%changelog
* Wed Aug 17 2022 YukariChiba <i@0x7f.cc> - 1.4.7-1
- Upgrade version to 1.4.7

* Tue May 10 2022 mylee <liweiganga@uniontech.com> - 1.4.5-3
- fix spec changelog date

* Sat Dec 18 2021 shixuantong<shixuantong@huawei.com> - 1.4.5-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix build fail 

* Thu Nov 11 2021 shixuantong<shixuantong@huawei.com> - 1.4.5-1
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:update version to 1.4.5

* Mon Jul 27 2020 wenzhanli<wenzhanli2@huawei.com> - 1.4.3-1
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:version update 1.4.3

* Sat Mar 21 2020 songnannan <songnannan2@huawei.com> - 1.4.2-2
- bugfix about update

* Mon Feb 17 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.4.2-1
- update to 1.4.2-1, drop python2 support

* Wed Sep 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.3.16-3
- Package init
