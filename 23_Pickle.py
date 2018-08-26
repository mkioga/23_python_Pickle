
# ==============
# 23_Pickle.py
# ==============

# In java, there is the concept of serialization.
# This is a process that allows objects to be saved to a file so that they can be
# restored from the file later.

# Python provides a method for serializating objects called pickling.
# When an object is pickled, it is written to a file format that contains the object data
# together with sufficient information to allow that object to be recreated when it is loaded back in.

# pickling is a much easier method of storing objects as compared to writing in binary


# import pickle module so we can use its library

import pickle

# We use a tuple to store imelda records

imelda = "More Mayhem", "Imelda May", 2011, (
          (1, "Pulling the rug"),
          (2, "Psycho"),
          (3, "Mayhem"),
          (4, "Kentish town walz"))

# print imelda tuple to see how it looks

print("imelda")
print(imelda)

# We open imelda.pickle (using pickle) then specify "wb" for write, to be saved to  pickle_file
# then use pickle.dump (to copy) from imelda to pickle_file
# if you double click "imelda.pickle" file created to the left, you will see it has data in a weird format

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)

# Now we can retrieve the data in "imelda.pickle" file we created
# We specify open("imelda.pickle", then "rb" for read and then save to file "imelda_pickled
# Then we use "pickle.load" to load data from "imelda_pickled" and save it to "imelda2"

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)

# Then we print "imelda2" and see it is same as original "imelda"

print()
print("imelda2")
print(imelda2)
print()

print("="*40)

# Then we unpack the tuple into 4 variables below and print

print("====== unpack the tuple ==========")
print()
album, artist, year, track_list = imelda2
print(album)
print(artist)
print(year)
print(track_list)
print()

# Since track_list is itself a tuple, we use a for loop to extract it.
print("======= Extract track =========")
print()
for track in track_list:
    track_number, track_title = track  # unpack
    print(track_number, track_title)    # print

print("="*40)

# =============================================================
# pickling many objects
# =============================================================


# Once you have opened a file for writing, you can pickle
# many objects as you want to in that one file

# We have a tuple

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the rug"),
    (2, "Psycho"),
    (3, "Mayhem"),
    (4, "Kentish town walz"))

# Then two lists

even = list(range(0, 10, 2))  # Make sure to create a list and then pass it a range
odd = list(range(1, 10, 2))


with open("imelda.pickle", "wb") as pickle_file:   # Save to pickle
    pickle.dump(imelda, pickle_file)      # pickle.dump ==> to store from imelda to pickle_file
    pickle.dump(even, pickle_file)        # store even list in pickle_file
    pickle.dump(odd, pickle_file)         # store odd list in pickle_file
    pickle.dump(2998302, pickle_file)     # can even store a number in same pickle_file

# NOTE: you can use any file to retrieve. we use imelda_pickled here
# NOTE: we retrieve in the same order they were stored

with open("imelda.pickle", "rb") as imelda_pickled:  # retrieve
    imelda2 = pickle.load(imelda_pickled)       # retrieve imelda from imelda_pickled
    even_list = pickle.load(imelda_pickled)     # retrieve even numbers
    odd_list = pickle.load((imelda_pickled))    # retrieve odd numbers
    x = pickle.load(imelda_pickled)             # retrieve the number we typed in

# Now we print the values we retrieved
print("===== unpacked imelda2 =======")
print()
album, artist, year, track_list = imelda2  # unpack imelda2 and print
print(album)
print(artist)
print(year)
print(track_list)

print("="*40)
print("=== extract songs in track ====")
print()
for track in track_list:   # use for loop to print track_list (a tuple in itself)
    track_number, track_title = track  # unpack
    print(track_number, track_title)    # print

print("=" *10)
for i in even_list:  # print even_list
    print(i)

print("=" *10)
for i in odd_list:  # print odd_list
    print(i)

print("=" *10)
print(x)  # print the number

print("="*40)

# =============================================================
# pickle protocols
# =============================================================


# NOTE: there are different protocols for pickling released with every python release
# Latest release is protocol version 4
# protocol version 3 is the default if we don't specify protocol
# These are not backward compatible. so if you pickle with an earlier protocol, you cannot retrieve with a later one


# We are going to use protocol 0 to store the objects

# We have a tuple

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the rug"),
    (2, "Psycho"),
    (3, "Mayhem"),
    (4, "Kentish town walz"))

# Then two lists

even = list(range(0, 10, 2))  # Make sure to create a list and then pass it a range
odd = list(range(1, 10, 2))


# Here we are going to use protocol 0
# run it and open the imelda.pickle file in the left. you will see it looks different from original one
# We can also specify default protocol and Highest (latest) protocol
# Python checks which protocol is used for each particular dump, so below works even if we specify different protocols

with open("imelda.pickle", "wb") as pickle_file:   # Save to pickle
    pickle.dump(imelda, pickle_file, protocol=0)        # we use protocol 0 to store
    pickle.dump(even, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)  # using default protocol
    pickle.dump(odd, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)   # using highest protocol
    pickle.dump(2998302, pickle_file, protocol=0)       #

# NOTE: you can use any file to retrieve. we use imelda_pickled here
# NOTE: we retrieve in the same order they were stored

with open("imelda.pickle", "rb") as imelda_pickled:  # retrieve
    imelda2 = pickle.load(imelda_pickled)       # retrieve imelda from imelda_pickled
    even_list = pickle.load(imelda_pickled)     # retrieve even numbers
    odd_list = pickle.load((imelda_pickled))    # retrieve odd numbers
    x = pickle.load(imelda_pickled)             # retrieve the number we typed in

# Now we print the values we retrieved
print("======= pickle protocols =======")
print()
album, artist, year, track_list = imelda2  # unpack imelda2 and print
print(album)
print(artist)
print(year)
print(track_list)
print()
for track in track_list:   # use for loop to print track_list (a tuple in itself)
    track_number, track_title = track  # unpack
    print(track_number, track_title)    # print

print("=" *10)
for i in even_list:  # print even_list
    print(i)

print("=" *10)
for i in odd_list:  # print odd_list
    print(i)

print("=" *10)
print(x)  # print the number




# =============================================================
# Security in pickling
# =============================================================

# protocol versions before version 2 performed a safety check when unpickling
# Here python would refuse to call functions or class distractors that were not marked as safe for pickling
# These checks were removed in version 2 on the basis that the security checks had not been extensively verified
# And there were many bugs that would have circumvented them
# So it was decided to be safer to publicize that pickling uses an insecure protocol rather than risking having
# people trusting a protocol that had not been completely checked.

# So you should only unpickle data that you can trust

# We will demonstrate how easy it is to wreck havoc by unpickling insecure data

# We will also discuss a different method of pickling and unpickling using the dump and load method
# but instead of writing or reading from a file, they send data to or get data from bytes objects (a sequence of bytes)


# We will create a rogue byte sequence that use pickle.load to delete a file

# pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.")    # "rm" is delete command for Mac/Linux.

# Before you run this, note that we have imelda.pickle file on the left
# After you run it, it deletes imelda.pickle file

# pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")   # "del" is delete command for Windows

# This would have been a huge security issue if you unpicked a bad code and it deleted your files.
# Here is the link with more details about pickle and a warning that pickle is not secure
# https://docs.python.org/2/library/pickle.html


