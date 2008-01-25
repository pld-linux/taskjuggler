#
# TODO:
#       - split package into two: taskjuggler and taskjuggler-kde
#         like in reference spec-file
#
Summary:	TaskJuggler - a project management tool
Summary(pl.UTF-8):	TaskJuggler - narzędzie do zarządzania projektami
Name:		taskjuggler
Version:	2.4.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.taskjuggler.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	d9076b5a1d2601f93ea4bc07780b7297
Source1:	http://www.taskjuggler.org/download/manual-%{version}.tar.bz2
# Source1-md5:	b1c1a04581dec6b6f4bdc274836041a5
Patch0:		kde-ac260-lt.patch
URL:		http://www.taskjuggler.org/
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-utils
BuildRequires:	jadetex
BuildRequires:	kdepim-devel >= 3.3
BuildRequires:	libxslt-devel
BuildRequires:	libxslt-progs
BuildRequires:	openjade
BuildRequires:	perl-Class-MethodMaker
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-PostScript-Simple
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-base
BuildRequires:	poster
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# kde3 apps need patching
%undefine	with_ccache

%define		specflags	-fno-strict-aliasing

%description
Taskjuggler is a project management tool for Linux and UNIX
system-based operating systems. Whether you want to plan your
colleague's shifts for the next month or want to build a skyscraper -
Taskjuggler is the tool for you. Instead of clicking yourself
painfully through hundreds of dialog boxes you specify your
Taskjuggler project in a simple text format. You simply list all your
tasks and their dependencies. The information is sent through
Taskjuggler and you will get all sorts of reports in HTML or XML
format. Taskjuggler does not only honor the task interdependencies but
also takes resource constrains into account. Using Taskjuggler's
powerful filtering and reporting algorithms you can create task lists,
resource usage tables, status reports, project calendars and project
accounting statements.

%description -l pl.UTF-8
Taskjuggler to narzędzie do zarządzania projektami dla Linuksa i
innych uniksowych systemów operacyjnych. Jest to narzędzie pozwalające
np. na zaplanowanie zmian kolegów w przyszłym miesiącu albo budowania
wieżowca. Zamiast bolesnego przeklikiwania się przez setki okienek
dialogowych przekazuje się projekt w prostym formacie tekstowym.
Wystarczy wypisać wszystkie zadania i ich zależności. Informacje są
przesyłane przez Taskjugglera, a użytkownik dostanie wszystkie rodzaje
raportów w formacie HTML lub XML. Taskjuggler nie tylko honoruje
wzajemne zależności zadań, ale także bierze pod uwagę ograniczenia
zasobów. Przy użyciu potężnego filtrowania i algorytmów raportowania
Taskjugglera można stworzyć listy zadań, tabele wykorzystania zasobów,
raporty o stanie, kalendarze projektów i oświadczenia rozliczające
projekty.

%prep
%setup -q -a1
%patch0 -p1

%build
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-kde-support=yes \
	--with-qt-libraries=%{_libdir} \
	--disable-rpath \
	--disable-final

# parallel make is broken in doc/en (looks like temporary file conflict)
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	docprefix=%{_docdir}/%{name}-%{version}/html \
	kdeprefix=%{_kdedocdir}/en/taskjuggler

%find_lang %{name} --with-kde

rm -f $RPM_BUILD_ROOT%{_libdir}/libtaskjuggler.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libtaskjuggler.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libtaskjuggler.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtaskjuggler.so.3
%{_desktopdir}/kde/*
%{_iconsdir}/*/*/*/*
%{_datadir}/apps/katepart/syntax/taskjuggler.xml
%{_datadir}/apps/%{name}
%{_datadir}/config/*
%{_datadir}/mimelnk/application/*
