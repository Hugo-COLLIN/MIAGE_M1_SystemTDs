// ---------------------------------------------------------------------
// Exercise inspiré du livre "Solutions Temps-Reel sous Linux"
// Blaess, C. (2019). Solutions temps réel sous Linux. Eyrolles.
// ---------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <sys/resource.h>

int main (int argc, char* argv[]){

   // ID du processus 
   int pid = getpid();   

   // variable pour mesurer le temps initial 
   time_t start;

   // nombre d'itérations exécutées
   long int nb_loops;			

   // valeur réference passée comme argument
   long int nb_loops_max;		

   // time() : nombre de secondes écoulées 
   // depuis le 1er janvier 1970 00:00:00 UTC
   start = time(NULL); 			 

   nb_loops = 0;			

   // Boucle de calcul pendant 10 s, pas d'E/S
   while (time(NULL) < (start + 10)){	 
      nb_loops ++;
   }

   // affiche le nombre d'itérations exécutées
   fprintf(stdout, "\n[Pid : %d] Nombre d'iterations : %ld", pid, nb_loops);

   // si la valeur référence est passée comme argument, 
   // comparer le nombre d'itérations exécutées avec celle-ci.
   if ((argc == 2) && (sscanf(argv[1], "%ld", &nb_loops_max) == 1)){
      fprintf(stdout, "\n[Pid : %d] Comparaison avec la valeur de référence : %ld / %ld ", pid, nb_loops, nb_loops_max);
      fprintf(stdout, " (%.8f %%)", 100.0*(float) nb_loops / nb_loops_max);
   }

   
   fprintf(stdout, "\n[%d] priority (%d) end \n", pid, getpriority(PRIO_PROCESS, pid));
   return EXIT_SUCCESS;
}
 
