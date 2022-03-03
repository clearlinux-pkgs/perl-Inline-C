#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Inline-C
Version  : 0.82
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETJ/Inline-C-0.82.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETJ/Inline-C-0.82.tar.gz
Summary  : 'C Language Support for Inline'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Inline-C-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::Copy::Recursive)
BuildRequires : perl(File::ShareDir::Install)
BuildRequires : perl(Inline)
BuildRequires : perl(Parse::RecDescent)
BuildRequires : perl(Pegex)
BuildRequires : perl(Pegex::Base)
BuildRequires : perl(Pegex::Parser)
BuildRequires : perl(Test::Warn)
BuildRequires : perl(YAML::XS)

%description
NAME
Inline::C - C Language Support for Inline
VERSION
This document describes Inline::C version 0.82.

%package dev
Summary: dev components for the perl-Inline-C package.
Group: Development
Provides: perl-Inline-C-devel = %{version}-%{release}
Requires: perl-Inline-C = %{version}-%{release}

%description dev
dev components for the perl-Inline-C package.


%package perl
Summary: perl components for the perl-Inline-C package.
Group: Default
Requires: perl-Inline-C = %{version}-%{release}

%description perl
perl components for the perl-Inline-C package.


%prep
%setup -q -n Inline-C-0.82
cd %{_builddir}/Inline-C-0.82

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Inline::C.3
/usr/share/man/man3/Inline::C::Cookbook.3
/usr/share/man/man3/Inline::C::ParsePegex.3
/usr/share/man/man3/Inline::C::ParseRecDescent.3
/usr/share/man/man3/Inline::C::ParseRegExp.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Inline/C.pm
/usr/lib/perl5/vendor_perl/5.34.0/Inline/C.pod
/usr/lib/perl5/vendor_perl/5.34.0/Inline/C/Cookbook.pod
/usr/lib/perl5/vendor_perl/5.34.0/Inline/C/ParsePegex.pod
/usr/lib/perl5/vendor_perl/5.34.0/Inline/C/ParseRecDescent.pod
/usr/lib/perl5/vendor_perl/5.34.0/Inline/C/ParseRegExp.pod
/usr/lib/perl5/vendor_perl/5.34.0/Inline/C/Parser.pm
/usr/lib/perl5/vendor_perl/5.34.0/Inline/C/Parser/Pegex.pm
/usr/lib/perl5/vendor_perl/5.34.0/Inline/C/Parser/Pegex/AST.pm
/usr/lib/perl5/vendor_perl/5.34.0/Inline/C/Parser/Pegex/Grammar.pm
/usr/lib/perl5/vendor_perl/5.34.0/Inline/C/Parser/RecDescent.pm
/usr/lib/perl5/vendor_perl/5.34.0/Inline/C/Parser/RegExp.pm
/usr/lib/perl5/vendor_perl/5.34.0/auto/share/dist/Inline-C/inline-c.pgx
