// ---------------------------------------------------------------------
// exemple-boucle-temps-reel.c
// Fichier d'exemple du livre "Solutions Temps-Reel sous Linux"
// (C) 2012-2015 Christophe BLAESS
// http://christophe.blaess.fr
// ---------------------------------------------------------------------

#define _GNU_SOURCE  // Pour avoir sched_setaffinity
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>


void child_process_function (int cpu);

int main(void)
{
	int number_of_cpus = sysconf(_SC_NPROCESSORS_ONLN);
	int cpu;

	for (cpu = 0; cpu < number_of_cpus; cpu ++) {
		if (fork() == 0) {
			child_process_function(cpu);
		}
	}
	/* Attendre la fin des fils */
	for (cpu = 0; cpu < number_of_cpus; cpu ++)
		waitpid(-1, NULL, 0);
	return EXIT_SUCCESS;
}


void child_process_function (int cpu)
{
	struct sched_param param;
	cpu_set_t  cpuset;

	/* Se placer sur le CPU indique */
	CPU_ZERO(& cpuset);
	CPU_SET(cpu, &cpuset);
	if (sched_setaffinity(0, sizeof(cpuset), & cpuset) !=0) {
		perror("sched_setaffinity");
		exit(EXIT_FAILURE);
	}
	/* Passer en temps-reel */
	param.sched_priority = 99;
	if (sched_setscheduler(0, SCHED_FIFO, & param) != 0) {
		perror("sched_setscheduler");
		exit(EXIT_FAILURE);
	}
	/* Dormir une seconde pour etre sur que tous les autres
	   processus sont sur leurs CPUs respectifs */
	sleep(1);
	/* Programmer une alarme dans 15 secondes */
	alarm(15);
	/* Boucler activement */
	while (1)
		;
}

