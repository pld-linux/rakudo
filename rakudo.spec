#
# STATUS:	does not build or run on a machine without parrot build tree
#		(~/rpm/BUILD/parrot-1.0.0 stuff)
#		the source of the problem is probably the current state of
#		parrot/libparrot.so

Summary:	Perl 6 implementation that runs on Parrot virtual machine
Summary(pl.UTF-8):Implementacja Perl 6 pracująca w środowisku maszyny Parrot
Name:		rakudo
Version:	0.0.2009.03
Release:	0.1
License:	The Artistic License 2.0
Group:		Applications
Source0:	http://www.pmichaud.com/perl6/%{name}-2009-03.tar.gz
# Source0-md5:	7faf255a9dd0cfcecb4b6362c1f32db5
URL:		http://rakudo.org
BuildRequires:	perl
Requires:	parrot
Provides:	perl6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rakudo Perl 6, or just Rakudo, is an implementation of the Perl 6
specification that will run on the Parrot virtual machine. Perl 6 is a
programming language standard. Unlike previous versions of Perl, it
will have multiple implementations.

%description -l pl.UTF-8
Rakudo Perl 6 lub po prostu Rakudo jest implementacją specyfikacji
języka Perl 6 przeznaczoną do pracy w środowisku maszyny wirtualnej
Parrot. Perl 6 jest pewnym standardem języka programowania. W
przeciwieństwie do poprzednich wersji Perla, ta będzie posiadała
wiele implementacji.

%prep
%setup -q -n %{name}-2009-03

%build
perl Configure.pl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install perl6 $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS LICENSE README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_bindir}/perl6
