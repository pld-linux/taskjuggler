#
# TODO:
#       - split package into two: taskjuggler and taskjuggler-kde
#         like in reference spec-file
#
Summary:	TaskJuggler - a project management tool
Summary(pl):	TaskJuggler - narzêdzie do zarz±dzania projektami
Name:		taskjuggler
Version:	2.2.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://www.taskjuggler.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	0f7a0301a6e1ec82378bbf4e2539af66
Source1:	http://www.taskjuggler.org/download/manual-%{version}.tar.bz2
# Source1-md5:	ea21fde74bced90946e9975fc7f68e57
Patch0:		%{name}-docbook.patch
URL:		http://www.taskjuggler.org/
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-utils
BuildRequires:	jadetex
BuildRequires:	kdepim-devel >= 3.3
BuildRequires:	libxslt-devel
BuildRequires:	libxslt-progs
BuildRequires:	openjade
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-Class-MethodMaker
BuildRequires:	perl-PostScript-Simple
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-base
BuildRequires:	poster
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
Taskjuggler to narzêdzie do zarz±dzania projektami dla Linuksa i
innych uniksowych systemów operacyjnych. Jest to narzêdzie pozwalaj±ce
np. na zaplanowanie zmian kolegów w przysz³ym miesi±cu albo budowania
wie¿owca. Zamiast bolesnego przeklikiwania siê przez setki okienek
dialogowych przekazuje siê projekt w prostym formacie tekstowym.
Wystarczy wypisaæ wszystkie zadania i ich zale¿no¶ci. Informacje s±
przesy³ane przez Taskjugglera, a u¿ytkownik dostanie wszystkie rodzaje
raportów w formacie HTML lub XML. Taskjuggler nie tylko honoruje
wzajemne zale¿no¶ci zadañ, ale tak¿e bierze pod uwagê ograniczenia
zasobów. Przy u¿yciu potê¿nego filtrowania i algorytmów raportowania
Taskjugglera mo¿na stworzyæ listy zadañ, tabele wykorzystania zasobów,
raporty o stanie, kalendarze projektów i o¶wiadczenia rozliczaj±ce
projekty.

%prep
%setup -q -a1
%patch0 -p1
:> docs/en/kde-doc.patch

%build
%configure \
	--with-kde-support=yes \
	--with-qt-libraries=%{_libdir} \
	--disable-rpath \
	--disable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	docprefix=%{_docdir}/%{name}-%{version}/html \
	kdeprefix=%{_kdedocdir}/en/taskjuggler

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*so.*.*.*
%{_desktopdir}/kde/*
%{_iconsdir}/*/*/*/*
%{_datadir}/apps/katepart/syntax/taskjuggler.xml
%{_datadir}/apps/%{name}
%{_datadir}/config/*
%{_datadir}/mimelnk/application/*
