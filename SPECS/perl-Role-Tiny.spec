Name:           perl-Role-Tiny
Version:        2.000006
Release:        2%{?dist}
Summary:        A nouvelle cuisine portion size slice of Moose
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/Role-Tiny/
Source0:        http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/Role-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Class::Method::Modifiers) >= 1.05
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
%if !%{defined perl_bootstrap}
# Cycle: perl-Role-Tiny → perl-namespace-autoclean → perl-Moose →
# perl-Test-Spelling → perl-Pod-Spell → perl-File-ShareDir-ProjectDistDir →
# perl-Path-IsDev → perl-Role-Tiny
BuildRequires:  perl(namespace::autoclean)
%endif
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Class::Method::Modifiers) >= 1.05
Requires:       perl(mro)

# perl-Role-Tiny was split from perl-Moo
Conflicts:      perl-Moo < 0.009014

%{?perl_default_filter}

%description
Role::Tiny is a minimalist role composition tool.

%prep
%setup -q -n Role-Tiny-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Role/
%{_mandir}/man3/Role::Tiny.3pm*
%{_mandir}/man3/Role::Tiny::With.3pm*

%changelog
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.000006-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 12 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.000006-1
- Update to 2.000006

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.000005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.000005-4
- Perl 5.26 re-rebuild of bootstrapped packages

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.000005-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.000005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 06 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 2.000005-1
- Update to 2.000005

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.000003-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.000003-2
- Perl 5.24 rebuild

* Fri May 06 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 2.000003-1
- Update to 2.000003

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.000001-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.000001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.000001-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.000001-2
- Perl 5.22 rebuild

* Sat Apr 25 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.000001-1
- Update to 2.000001

* Sun Mar 01 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.000000-1
- Update to 2.000000

* Mon Nov 10 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 1.003004-1
- Update to 1.003004

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.003003-4
- Perl 5.20 re-rebuild of bootstrapped packages

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.003003-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.003003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 29 2014 Paul Howarth <paul@city-fan.org> - 1.003003-1
- Update to 1.003003
  - Overloads specified as method names rather than subrefs are now applied
    properly
  - Allow superclass to provide conflicting methods (CPAN RT#91054)
  - Use ->is_role internally to check if a package is a role
  - Document that Role::Tiny applies strict and fatal warnings
- Require Class::Method::Modifiers at runtime
- Make %%files list more explicit

* Tue Mar 25 2014 Petr Pisar <ppisar@redhat.com> - 1.003002-2
- Break build-cycle: perl-Role-Tiny → perl-namespace-autoclean → perl-Moose →
  perl-Test-Spelling → perl-Pod-Spell → perl-File-ShareDir-ProjectDistDir →
  perl-Path-IsDev → perl-Role-Tiny

* Fri Oct 18 2013 Miro Hrončok <mhroncok@redhat.com> - 1.003002-1
- 1.003002 bump

* Fri Aug 16 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.003001-1
- 1.003001 bump
- Specify all dependencies

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.002005-2
- Perl 5.18 rebuild

* Fri Feb 15 2013 Iain Arnell <iarnell@gmail.com> 1.002005-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.002004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 02 2012 Iain Arnell <iarnell@gmail.com> 1.002004-1
- update to latest upstream version

* Sun Oct 28 2012 Iain Arnell <iarnell@gmail.com> 1.002002-1
- update to latest upstream version

* Sat Oct 27 2012 Iain Arnell <iarnell@gmail.com> 1.002001-1
- update to latest upstream version

* Sat Oct 20 2012 Iain Arnell <iarnell@gmail.com> 1.002000-1
- update to latest upstream version

* Sun Jul 29 2012 Iain Arnell <iarnell@gmail.com> 1.001005-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.001004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Iain Arnell <iarnell@gmail.com> 1.001004-1
- update to latest upstream version

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 1.001002-2
- Perl 5.16 rebuild

* Tue May 08 2012 Iain Arnell <iarnell@gmail.com> 1.001002-1
- update to latest upstream version

* Fri Apr 27 2012 Iain Arnell <iarnell@gmail.com> 1.001001-1
- update to latest upstream version
- don't explicity require Class::Method::Modifiers

* Wed Apr 04 2012 Iain Arnell <iarnell@gmail.com> 1.000001-1
- update to latest upstream version

* Mon Apr 02 2012 Iain Arnell <iarnell@gmail.com> 1.000000-3
- explicitly conflict with perl-Moo < 0.009014; this module used to be
  distributed as part of Moo

* Mon Apr 02 2012 Iain Arnell <iarnell@gmail.com> 1.000000-2
- fix spelling of cuisine in summary

* Sun Apr 01 2012 Iain Arnell <iarnell@gmail.com> 1.000000-1
- Specfile autogenerated by cpanspec 1.79.
