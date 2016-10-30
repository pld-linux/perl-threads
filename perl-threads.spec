#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	threads
%include	/usr/lib/rpm/macros.perl
Summary:	threads - Perl interpreter-based threads
Name:		perl-threads
Version:	2.01
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JD/JDHEDDEN/threads-%{version}.tar.gz
# Source0-md5:	aec3a036c31ffa868adda1170ef26240
URL:		http://search.cpan.org/dist/threads/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Since Perl 5.8, thread programming has been available using a model
called interpreter threads which provides a new Perl interpreter for
each thread, and, by default, results in no data or state information
being shared between threads.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/threads.pm
%dir %{perl_vendorarch}/auto/threads
%attr(755,root,root) %{perl_vendorarch}/auto/threads/threads.so
%{_mandir}/man3/threads.3pm*
%{_examplesdir}/%{name}-%{version}
