# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SG2000'
copyright = '2023 SOPHGO Co., Ltd'
author = 'Sophgo'
release = '1.0-alpha'
release_date = '2023-11-22'

title = '技术参考手册'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

latex_maketitle = r'''
		\begin{titlepage}
		\begin{center}
		\includegraphics[width=0.4\textwidth]{SOPHON-LOGO.png}
		\vspace*{2cm}

		\Huge \textbf{'''+ project + r'''} \par
		\vspace*{1cm}
		\Huge \textbf{'''+ title + r'''} \par
		\vspace*{4cm}
		\end{center}
		\noindent \Large 版本 : ''' + release + r'''\par
		\noindent \Large 发布日期 : ''' + release_date + r'''\par
		\vspace*{2cm}
		\noindent \normalsize Copyright © ''' + copyright + r'''. All rights reserved.\\
		\end{titlepage}'''

latex_preamble = r'''
		\usepackage{tocloft}
		\usepackage[document]{ragged2e}
		\newcommand{\sectionbreak}{\clearpage}
		\renewcommand\cftfignumwidth{4em}
		\renewcommand\cfttabnumwidth{4em}
		\renewcommand\cftsecnumwidth{4em}
		\renewcommand\cftsubsecnumwidth{6em}
		\renewcommand\cftparanumwidth{6em}
		\usepackage{fancyhdr}
		\setlength\headheight{14pt}
		\fancypagestyle{normal}{
			\fancyhead[R]{}
			\fancyhead[C]{\leftmark}
			\fancyfoot[C]{Copyright © ''' + copyright + r'''}
			\fancyfoot[R]{\thepage}
			\renewcommand{\headrulewidth}{0.4pt}
			\renewcommand{\footrulewidth}{0pt}
		}'''

latex_elements = {
	'maketitle': latex_maketitle,

	'preamble': latex_preamble,
}

number_figures = True
numfig = True
numfig_secnum_depth = 1
numfig_format = {'figure': '图%s', 'code-block': '程序清单%s', 'table': '表%s'}