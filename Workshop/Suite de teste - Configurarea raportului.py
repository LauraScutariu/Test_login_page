"""
In interiorul metodei definite anterior va trebui sa definim un runner care sa contina parametrii de configurare ai raportului de executie:

runner = HtmlTestRunner.HTMLTestRunner
        (
            combine_reports=True, # daca avem mai multe clase de test, rezultatele vor fi puse in acelasi raport de executie
            report_title='TestReport',
            report_name='Smoke Test Result'
        )

Pentru a putea avea acest runner functional trebuie sa instalam (pip install html-testRunner) si sa importam (import HtmlTestRunner)
libraria aferenta.

Dupa cum observati, runner este un obiect instantiat din clasa HTMLTestRunner care a primit drept argumente valorile combine_reports, report_title si report_name.

Ultimul pas va fi sa apelam runnerul care va primi drept argument lista de teste de rulat: runner.run(test_de_rulat).

Observati cum dupa rulare in meniul din stanga a aparut raportul de executie.

Experimentati putin cu diverse teste si observati cum se schimba raportul de executie.

"""