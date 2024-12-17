// ---------------------------------------------------------------------
// Exercise inspiré du livre "Solutions Temps-Reel sous Linux"
// Blaess, C. (2019). Solutions temps réel sous Linux. Eyrolles.
// ---------------------------------------------------------------------

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>


void * thread_function (void * arg)
{
	long nice_value = (long) arg;
	time_t start;
	long nb_loops = 0;

	// nice() : ajoute l'argument à la valeur nice du thread appelant. 
	// (UNE une valeur nice plus élevée signifie une priorité inférieure.)  
	nice(nice_value);

	// time() : nombre de secondes écoulées 
	// depuis le 1er janvier 1970 00:00:00 UTC
	start = time(NULL);

	// Boucle de calcul pendant 10 s, pas d'E/S
	while (time(NULL) < (start + 10))
		nb_loops ++;

	return (void *) nb_loops;
}

#define NB_THREADS  5

int main(void)
{
	int i;
	void * result;
	long nice_value[NB_THREADS];
	pthread_t thread[NB_THREADS];
	long loops_count = 0;
	long nb_loops[NB_THREADS];

	// selection des valeurs nice
	for (i = 0; i < NB_THREADS; i ++){
		nice_value[i] = (i+1) * (20 / NB_THREADS);
		printf("Thread %d, nice %ld\n", i, nice_value[i]);
	}

	// instatiation des threads
	for (i = 0; i < NB_THREADS; i ++)
		pthread_create(& (thread[i]), NULL, thread_function, (void *) nice_value[i]);

	// attend que les threads se terminent	               
	for (i = 0; i < NB_THREADS; i ++) {
		pthread_join(thread[i], & result);
		nb_loops[i] = (long) result;
		loops_count += nb_loops[i];
	}

	// affiche les résultats de l'exécution 
	for (i = 0; i < NB_THREADS; i ++)
		printf("Thread %d, nice %ld, nombre d'iterations = %ld (%.0f %%)\n",
			i, 
			nice_value[i],
			nb_loops[i],
			100.0 * nb_loops[i] / loops_count);

	return EXIT_SUCCESS;
}
