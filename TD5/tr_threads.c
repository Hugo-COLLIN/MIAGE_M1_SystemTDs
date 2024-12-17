// ---------------------------------------------------------------------
// Exercise inspiré du livre "Solutions Temps-Reel sous Linux"
// Blaess, C. (2019). Solutions temps réel sous Linux. Eyrolles.
// ---------------------------------------------------------------------

#include <pthread.h>
#include <sched.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/time.h>

#define NB_THREADS 4

void * thread_function(void * arg)
{
	long int id = (long int) arg;
	int i, j;

	sleep(id*2);

	fprintf(stderr, "Thread %ld commence à %ld\n", id, time(NULL));
	for (i = 0; i < 500000; i ++)
		for (j = 0; j < 10000; j ++)
			;
	fprintf(stderr, "Thread %ld se termine à %ld\n", id, time(NULL));
	return NULL;
}

int main(void)
{
	long int i;
	int err;
	pthread_attr_t attr;
	struct sched_param param;
	pthread_t thr[NB_THREADS];

	// Fixe la valeur par défaut pour tous le attribus
	pthread_attr_init (& attr);

	// Inscrit l'ordonnancement dans les attribus
	if ((err = pthread_attr_setschedpolicy(& attr, SCHED_FIFO)) != 0) {
		fprintf(stderr, "setschedpolicy: %s\n", strerror(err));
		exit(EXIT_FAILURE);
	}
	// Le thread est ordonnancé en fonction des attributs indiqués dans l'object "attr"
	if ((err = pthread_attr_setinheritsched(& attr, PTHREAD_EXPLICIT_SCHED)) != 0) {
		fprintf(stderr, "setinheritsched: %s\n", strerror(err));
		exit(EXIT_FAILURE);
	}
	for (i = 0; i < NB_THREADS; i ++) {
		// Choisir la priorité temps réel 
		param.sched_priority = (i + 1) * 10;
		if ((err = pthread_attr_setschedparam(& attr, & param)) != 0) {
			fprintf(stderr, "setschedparam: %s\n", strerror(err));
			exit(EXIT_FAILURE);
		}
		fprintf(stderr, "Thread %ld a la priorité de %d\n", i+1, param.sched_priority);
		//Créer un thread avec les attribus précisés 
		if ((err = pthread_create(& (thr[i]), & attr, thread_function, (void *) (i+1))) != 0) {
			fprintf(stderr, "pthread_create: %s\n", strerror(err));
			exit(EXIT_FAILURE);
		}
	}
	for (i = 0; i < NB_THREADS; i ++)
		pthread_join(thr[i], NULL);

	return EXIT_SUCCESS;
}

